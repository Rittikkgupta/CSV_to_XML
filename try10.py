import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

reservation_data = pd.read_csv('t/reservation.csv', encoding='ISO-8859-1')
people_data = pd.read_csv('t/people.csv', encoding='ISO-8859-1')
hotel_data = pd.read_csv('t/hotel.csv', encoding='ISO-8859-1')
client_data = pd.read_csv('t/client.csv', encoding='ISO-8859-1')
service_data = pd.read_csv('t/service.csv', encoding='ISO-8859-1')
client_service_data = pd.read_csv('t/clientservice.csv', encoding='ISO-8859-1')



        

for _, reservation_row in reservation_data.iterrows():
    now=datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S.%f")
    root = ET.Element('RESERVATIONS')
    reservation = ET.SubElement(root, 'RESERVATION',
                                NUMBER=str(reservation_row['NUMBER']),
                                DATE=str(reservation_row['DATE']),
                                BEG=str(reservation_row['BEG']),
                                END=str(reservation_row['END']),
                                PARTNER_INC=str(reservation_row['PARTNER_INC']),
                                PARTNER=str(reservation_row['PARTNER']),
                                PARTNER_CONTRACT=str(reservation_row['PARTNER_CONTRACT']),
                                PARTNER_INN=str(reservation_row['PARTNER_INN']),
                                TOUR_INC=str(reservation_row['TOUR_INC']),
                                TOUR=str(reservation_row['TOUR']),
                                NOTE=str(reservation_row['NOTE']),
                                DEPTSUM=str(reservation_row['DEPTSUM']),
                                DEPTCURRENCY=str(reservation_row['DEPTCURRENCY']),
                                PROFITSUM=str(reservation_row['PROFITSUM']),
                                PROFITCURRENCY=str(reservation_row['PROFITCURRENCY']),
                                STATUS_INC=str(reservation_row['STATUS_INC']),
                                STATUS=str(reservation_row['STATUS']),
                                PARTNER_TOWN_INC=str(reservation_row['PARTNER_TOWN_INC']),
                                PARTNER_TOWN=str(reservation_row['PARTNER_TOWN']),
                                PARTNER_STATE_INC=str(reservation_row['PARTNER_STATE_INC']),
                                PARTNER_STATE=str(reservation_row['PARTNER_STATE']))

    peoples = ET.SubElement(reservation, 'PEOPLES')
    for _, people_row in people_data[people_data['NUMBER'] == reservation_row['NUMBER']].iterrows():
        people = ET.SubElement(peoples, 'PEOPLE',
                               ID=str(people_row['ID']),
                               HUMAN=str(people_row['HUMAN']),
                               NAME=str(people_row['NAME']),
                               LNAME=str(people_row['LNAME']),
                               PNUMBER=str(people_row['PNUMBER']),
                               PSER=str(people_row['PSER']),
                               GENDER=str(people_row['GENDER']))

    hotels = ET.SubElement(reservation, 'HOTELS')
    for _, hotel_row in hotel_data[hotel_data['NUMBER'] == reservation_row['NUMBER']].iterrows():
        hotel = ET.SubElement(hotels, 'HOTEL',
                              ID=str(hotel_row['ID']),
                              BEG=str(hotel_row['BEG']),
                              END=str(hotel_row['END']),
                              HOTEL_INC=str(hotel_row['HOTEL_INC']),
                              HOTEL=str(hotel_row['HOTEL']),
                              ROOM_INC=str(hotel_row['ROOM_INC']),
                              ROOM=str(hotel_row['ROOM']),
                              PLACE_INC=str(hotel_row['PLACE_INC']),
                              PLACE=str(hotel_row['PLACE']),
                              MEAL_INC=str(hotel_row['MEAL_INC']),
                              MEAL=str(hotel_row['MEAL']),
                              CNT=str(hotel_row['CNT']),
                              PARTNER_INC=str(hotel_row['PARTNER_INC']),
                              PARTNER=str(hotel_row['PARTNER']),
                              PARTNER_INN=str(hotel_row['PARTNER_INN']),
                              NETPRICE=str(hotel_row['NETPRICE']),
                              NETPRICEDETAIL=str(hotel_row['NETPRICE']),
                              NETCURRENCY_INC=str(hotel_row['NETCURRENCY_INC']),
                              NETCURRENCY=str(hotel_row['NETCURRENCY']),
                              SALEPRICE=str(hotel_row['SALEPRICE']),
                              SALEPRICEDETAIL=str(hotel_row['SALEPRICEDETAIL']),
                              SALECURRENCY_INC=str(hotel_row['SALECURRENCY_INC']),
                              SALECURRENCY=str(hotel_row['SALECURRENCY']),
                              ACTSTATUS_INC=str(hotel_row['ACTSTATUS_INC']),
                              ACTSTATUS=str(hotel_row['ACTSTATUS']),
                              HOTEL_TOWN_INC=str(hotel_row['HOTEL_TOWN_INC']),
                              HOTEL_TOWN=str(hotel_row['HOTEL_TOWN']),
                              HOTEL_STATE_INC=str(hotel_row['HOTEL_STATE_INC']),
                              HOTEL_STATE=str(hotel_row['HOTEL_STATE']),
                              PARTNER_TOWN_INC=str(hotel_row['PARTNER_TOWN_INC']),
                              PARTNER_TOWN=str(hotel_row['PARTNER_TOWN']),
                              PARTNER_STATE_INC=str(hotel_row['PARTNER_STATE_INC']),
                              PARTNER_STATE=str(hotel_row['PARTNER_STATE']))

        clients = ET.SubElement(hotel, 'CLIENTS')
        for _, client_row in client_data[client_data['HOTEL ID'] == hotel_row['ID']].iterrows():
            client = ET.SubElement(clients, 'CLIENT',
                                ID=str(client_row['CLIENT ID']),
                                PEOPLEID=str(client_row['PEOPLEID']),
                                COMMON=str(client_row['COMMON']))
            
    services = ET.SubElement(reservation, 'SERVICES')
    for _, service_row in service_data[service_data['NUMBER'] == reservation_row['NUMBER']].iterrows():
        service = ET.SubElement(services, 'SERVICE',
                              ID=str(service_row['ID']),
                              BEG=str(service_row['BEG']),
                              END=str(service_row['END']),
                              SERVICE_INC=str(service_row['SERVICE_INC']),
                              SERVICE=str(service_row['SERVICE']),
                              SERVICETYPE_INC=str(service_row['SERVICETYPE_INC']),
                              SERVICETYPE=str(service_row['SERVICETYPE']),
                              CNT=str(service_row['CNT']),
                              PARTNER_INC=str(service_row['PARTNER_INC']),
                              PARTNER=str(service_row['PARTNER']),
                              PARTNER_INN=str(service_row['PARTNER_INN']),
                              SALEPRICE=str(service_row['SALEPRICE']),
                              SALEPRICEDETAIL=str(service_row['SALEPRICEDETAIL']),
                              SALECURRENCY_INC=str(service_row['SALECURRENCY_INC']),
                              SALECURRENCY=str(service_row['SALECURRENCY']),
                              
                              ACTSTATUS_INC=str(service_row['ACTSTATUS_INC']),
                              ACTSTATUS=str(service_row['ACTSTATUS']),
                              PARTNER_TOWN_INC=str(service_row['PARTNER_TOWN_INC']),
                              PARTNER_TOWN=str(service_row['PARTNER_TOWN']),
                              PARTNER_STATE_INC=str(service_row['PARTNER_STATE_INC']),
                              PARTNER_STATE=str(service_row['PARTNER_STATE']))
        clients = ET.SubElement(service, 'CLIENTS')
        for _, client_row in client_service_data[client_service_data['ID'] == service_row['ID']].iterrows():
            client = ET.SubElement(clients, 'CLIENT',
                                ID=str(client_row['CLIENT ID']),
                                PEOPLEID=str(client_row['PEOPLEID']))
                                
                               
                              
    xml_string = ET.tostring(root, 'utf-8')
    xml_pretty = minidom.parseString(xml_string).toprettyxml(indent="  ")
    filename = f"reservation_{reservation_row['NUMBER']}_{dt_string}.xml"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(xml_pretty)



