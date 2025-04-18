from os import name
from typing import Optional, Dict, BinaryIO, Any
from datetime import datetime

from lxml import etree
from lxml.etree import ElementBase, ElementTree

from core.usecases import BaseUC
from core.entities import Building, Unit, Floor, Room
from core.dependencies import IBuildingCRUD, IUnitCRUD, IFloorCRUD, IRoomCRUD, IFileStorage



class InitBuilding(BaseUC):
    svg_schema: Any
    _building_crud: IBuildingCRUD
    _unit_crud: IUnitCRUD
    _floor_crud: IFloorCRUD
    _room_crud: IRoomCRUD
    _fstorage: IFileStorage

    @classmethod
    def set_dependencies(cls,
                         building_crud: IBuildingCRUD,
                         unit_crud: IUnitCRUD,
                         floor_crud: IFloorCRUD,
                         room_crud: IRoomCRUD,
                         file_storage: IFileStorage) -> 'InitBuilding':
        cls._building_crud: IBuildingCRUD = building_crud
        cls._unit_crud: IUnitCRUD = unit_crud
        cls._floor_crud: IFloorCRUD = floor_crud
        cls._room_crud: IRoomCRUD = room_crud
        cls._fstorage: IFileStorage = file_storage
        return cls
    

    async def execute(self) -> Building:
        data = await self.svg_schema.read()
        root = etree.XML(data, etree.XMLParser())

        schema_uri = await self._fstorage.save_file(self.svg_schema, self.svg_schema.filename)

        xml_building: ElementBase = root.xpath('descendant::*[@type=\'building\']')[0]

        building = await self._building_crud.create_building(
            name=xml_building.get('building-name'),
            description=xml_building.get('building-description'),
            geopoint_lt=xml_building.get('geopoint-lt'),
            geopoint_rb=xml_building.get('geopoint-rb'),
            schema_uri=schema_uri
        )
        
        xml_units: list[ElementBase] = xml_building.xpath('descendant::*[@type=\'unit\']')

        for u in xml_units:
            unit = await self._unit_crud.create_unit(
                name=u.get('unit-name'),
                building_id=building.buildingID,
                description=u.get('unit-description')
            )
            
            xml_floors: list[ElementBase] = u.xpath('descendant::*[@type=\'floor\']')
            
            for f in xml_floors:
                floor = await self._floor_crud.create_floor(
                    name=f.get('floor-name'),
                    sequence=int(f.get('floor-level')),
                    unit_id=unit.unitID
                )

                xml_rooms: list[ElementBase] = f.xpath('descendant::*[@type=\'room\']')
                
                for r in xml_rooms:
                    room = await self._room_crud.create_room(
                        name=r.get('room-name'),
                        description=r.get('room-description'),
                        floor_id=floor.floorID
                    )
        
        return building
