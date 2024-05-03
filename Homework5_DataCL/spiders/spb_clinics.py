import scrapy


class SpbClinicsSpider(scrapy.Spider):
    name = "spb_clinics"
    allowed_domains = ["zdrav.spb.ru"]
    start_urls =[f"http://zdrav.spb.ru/ru/institutions/?page={i}" for i in range(1,32)]
            
    
    def parse(self, response):
        clinics = response.xpath("//li/div")
        for clinic in clinics:
            name = clinic.xpath(".//span/h4/a/text()").get().strip('\n')
            type = clinic.xpath(".//span/em/text()").get().split('/')[0].strip()
            district = clinic.xpath(".//span/em/text()").get().split('/')[1].strip()
            phone = clinic.xpath(".//span/p[1]/text()").get().strip('\n')
            address = clinic.xpath(".//span/p[2]/text()").get()            
        
            yield {
                'name' : name,
                'type' : type,
                'district': district,
                'phone' : phone,
                'address' : address
            }
        
