from urllib import robotparser

#robots.txt dosyasının bulunduğu adres.
ROBOT_PROTOCOL_URL = 'https://www.hepsiburada.com/robots.txt'

#robotFileParser örneğinin yaratılması ve robots.txt dosyasının adresten istenmesi.
robot_parser = robotparser.RobotFileParser(ROBOT_PROTOCOL_URL)

#read() robots.txt dosyasını okur.
robot_parser.read()

#can_fetch(useragent, url) parametrelerini alıyor ve 
#bize verilen user-agent için istenen url in izni olup olmadığı bilgisini döndürüyor.

robot_parser.can_fetch('*','/kiyasla/')
#False

robot_parser.can_fetch('*', '/product/')
#False

robot_parser.can_fetch('*', '/')
#True

robot_parser.can_fetch('*', '/uyelik/')
#True