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
        xml_root = etree.XML(data, etree.XMLParser())

        schema_uri = await self._fstorage.save_file(self.svg_schema, self.svg_schema.filename)

        xml_building: ElementBase = xml_root.xpath('descendant::*[@type=\'building\']')[0]

        building = Building(
            buildingID=xml_building.get('building-id'),
            buildingName=xml_building.get('building-name'),
            buildingDescription=xml_building.get('building-description'),
            geopointLT=xml_building.get('geopoint-lt'),
            geopointRB=xml_building.get('geopoint-rb'),
            svg_schema=schema_uri,
            units=[]
        )
        
        xml_units: list[ElementBase] = xml_building.xpath('descendant::*[@type=\'unit\']')

        for u in xml_units:
            unit = Unit(
                unitID=u.get('unit-id'),
                unitName=u.get('unit-name'),
                unitDescription=u.get('unit-edscription'),
                buildingID=building.buildingID,
                floors=[]
            )
            
            xml_floors: list[ElementBase] = u.xpath('descendant::*[@type=\'floor\']')
            
            for f in xml_floors:
                floor = Floor(
                    floorID=f.get('floor-id'),
                    floorName=f.get('floor-name'),
                    floorSequence=int(f.get('floor-level')),
                    unitID=unit.unitID,
                    rooms=[]
                )

                xml_rooms: list[ElementBase] = f.xpath('descendant::*[@type=\'room\']')
                
                for r in xml_rooms:
                    room = Room(
                        roomID=r.get('room-id'),
                        romName=r.get('room-name'),
                        roomDescription=r.get('room-description'),
                        floorID=floor.floorID
                    )

                    floor.rooms.append(room)

                unit.floors.append(floor)
            
            building.units.append(unit)
        
        building = await self._building_crud.save_building(building=building)

        building = await self._building_crud.get_building_by_id(building_id=building.buildingID)
        
        return building
