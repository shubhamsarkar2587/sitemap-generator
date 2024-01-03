from api_module import get_api_data
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime
from urllib.parse import quote


api_endpoint = ""
token = ""

api_data = get_api_data(api_endpoint, token)
req_data = api_data["data"][0]["result"]

# Create XML structure
urlset = ET.Element("urlset")
urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

for page in req_data:
    url = ET.SubElement(urlset, "url")

    loc = ET.SubElement(url, "loc")
    loc.text = "https://www.growder.com/view-product/" + quote(page["product_name"])

    current_datetime = datetime.utcnow()
    formatted_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%S+00:00")
    lastmod = ET.SubElement(url, "lastmod")
    lastmod.text = formatted_datetime

    changefreq = ET.SubElement(url, "changefreq")
    changefreq.text = "monthly"

    priority = ET.SubElement(url, "priority")
    priority.text = "0.9"

# Create XML tree and write to file
tree = ET.ElementTree(urlset)
xml_str = ET.tostring(tree.getroot(), encoding="utf-8", method="xml")
xml_pretty_str = minidom.parseString(xml_str).toprettyxml(indent="  ", encoding="utf-8")
with open("sitemap.xml", "wb") as file:
    file.write(xml_pretty_str)
