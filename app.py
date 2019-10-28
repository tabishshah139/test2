import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
import time
from itertools import cycle
from discord.utils import get
from discord import Game
import os

from discord import Activity, ActivityType


client = commands.Bot(command_prefix='+')
#client = discord.Client()
Clientdiscord = discord.Client()


#create an arraylist containing phrases you want your bot to switch through.
status = cycle(['+help', '+stock', '+spotify', '+origin', '+steam', '+hulu', '+fortnite', '+minecraft', '+uplay', 'wwe', 'pornhub', 'mail'])

client.remove_command('help')

# this is only for test if bot working
@client.event
async def on_message(message):
    message.content = message.content.lower()
    author = '{0.author.mention}'.format(message)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

# this lines you can modify  

    if message.content.startswith('+hello'):
        msg = 'Hello python {0.author.mention}'.format(message)
        await message.author.send(msg)


    if message.content.startswith('+invite'):
        await message.author.send("Click To Invite Bot In Your Server https://discordapp.com/api/oauth2/authorize?client_id=619923933109420097&permissions=0&scope=bot")

    if message.content.startswith('+help'):
        await message.author.send("Introducing TABISH SHAH BOT")
        await message.author.send("You Can Invite This Bot To Your Server +invite")
        await message.author.send("Rare Account Generating Bot")
        await message.author.send("You Can Check Available Stock In BOT +stock")


    if message.content.startswith('+fortnite'):
        randomlist = ['youngmulah49@yahoo.com:Aceisb123','sanjibmegh@gmail.com:sanjibmegh78','cavecow878@gmail.com:ryebread1','kayciegiles@gmail.com:soccergirl78','avoegm@gmail.com:11co1w9upi','caithss@gmail.com:dd6ad66','heineken_barcelona@hotmail.com:heineken12','jeanpot4545@gmail.com:Lankie10','alejandrob111@hotmail.com:Neongreen12','jakewheal@hotmail.co.uk:SUPERM4N1','robert.parker@bell.net:Roma2601','ashley.swim18@gmail.com:HMSTdhr2','niyaun@msn.com:sting455','diego.vargas1118@gmail.com:boombom1','ziuzad@gmail.com:sheepa1994','domen.sustaric@gmail.com:Racunalnica1','thoms.colombo@gmail.com:toto1994','weistart.ryan@hotmail.com:147853Ry','miguelamartinez0224@gmail.com:dreamchasing09','rowanhamdouglas@gmail.com:Hamilton1!','Cjjchickey178@gmail.com:paint123','spaikesalonika@hotmail.com:spaikeole1','salwanarjun@gmail.com:DrJackal@05','Robertsingh67@gmail.com:Yankees2','cheesee12@gmail.com:Chrisi96','ian0008@hotmail.com:godfrey23','crunch.matic23@gmail.com:Dsavage23','id4shopping@gmail.com:Gustnsh84','dazedconfuzed11@gmail.com:Strange1love','jasonroivas@gmail.com:superman08','sargolinibrody12@gmail.com:Brody123','C.keioglian@yahoo.com:Fuckoff1','gas.ezequieldiaz@gmail.com:totito91','sgarvey99@gmail.com:diamond2001','stepanov.george@gmail.com:Madzigon1','paulnelson8@hotmail.com:Bruins11','maharned02@gmail.com:Lifeisgood010101!','xaviermattingly@yahoo.com:Xm101690','jan130798.55@gmail.com:nintendo1307','cberesford422@gmail.com:colin1196','stephen.martinez728@gmail.com:Steve741.','jruzza89@gmail.com:Ciaosusy1','colin.simonetta@gmail.com:bongbong22','slim9081@hotmail.com:Tagboy12','thomasbohnhorst@gmx.de:Bohni100','jaosn11214@gmail.com:Jasonmei123','brendasano@gmail.com:network1.','jackhalpin@ymail.com:redbull1231','damiencopeland@gmail.com:D6210696!','rob.stal@hotmail.com:Prullenbak1','marc.bourgier@hotmail.fr:Namar666','mamalucco@gmail.com:ilpassero81','pounder08@hotmail.com:Kp16051990','autumnsummers1@hotmail.com:Ilkailka17','ritagarmi@gmail.com:penaguila7','krat654@gmail.com:vlad2004','jalen99@live.com:Masterkey1234','mimic.972@hotmail.fr:Souris55','rachelfortt@yahoo.co.uk:oliver2007','brescoach@gmail.com:Maddux31!','sunnygeegee@gmail.com:Dogpoop123a','sanji1209@gmail.com:tkdals43','piko29minecraft@gmail.com:piko0228','somakasan@yandex.ru:somakasan1','holz.leonie@web.de:Celinale1','meandmy2jlvs@yahoo.com:Stealth123!','andykang01@hotmail.com:Superhigh1!','spardinu69@gmail.com:qwerty21','emiliebouman@gmail.com:Mismus0078','rockylong84@gmail.com:Hendrix84','alonso_07-10@hotmail.com:Jklfds0710','melialava2006@gmail.com:meli2006','aryan2012amit@gmail.com:deepraj1','wielokropek6@gmail.com:szyk2000','priscillaberstler@aol.com:tycoon1','pedobaer007@hotmail.com:Gaggi123','alexr0x@gmail.com:As056999420','p.berger1990@web.de:O1o11oo1','petergiampaoli@gmail.com:ginger86','jday216@gmail.com:leahbaby216','rgchapman21@gmail.com:michelle926','aittor_herndz09@hotmail.com:Badajocense9.','jasoncartwright96@gmail.com:12345jason','justin.hall12@yahoo.com:Sprint10','markus.maul92@gmail.com:Handball1','fera.marsh@gmail.com:Kambenk1992','tophergrafixs@gmail.com:1jasmyn','eje0203@gmail.com:cetw1993','b.rod94@hotmail.com:brod0794','dalehall17@gmail.com:rodger11','cemmons08@gmail.com:Danger123','harleesuggs@yahoo.com:smokey1997','e.swag923@gmail.com:rosasse10','sanheim.sama@gmail.com:JuanDeJuanes16','gagesj1210@yahoo.com:Gage1210','brunoqueado2004@hotmail.com:lesluthiers3','ttc123401321@gmail.com:abc01321','gaara9518@gmail.com:gaara1795','jessicabuser@gmx.ch:Sultan123','edwardh0922@gmail.com:Oldhouse1','leandrorebellato@gmail.com:dieguito1','benlmaden@hotmail.co.uk:autumn91','darkthony@hotmail.com:hermanos12','razva.bebe@gmail.com:Delian12','dylansulak@gmail.com:doolie21','chrissocci901@gmail.com:iliketurtlez123','mimiche66@hotmail.com:LILIAN2005','4mcgovern.dillon@gmail.com:ironman6','colten_stephens@hotmail.com:Speeder1','brescina00@hotmail.com:anna1234','alejandroamarof@gmail.com:padres011','jaylynkinslow880@gmail.com:Jck828800','makayla.knott@yahoo.com.au:Rapalas09','cinus.marco@libero.it:Eugenio89','jmtguimaraes@gmail.com:Putavida1','cody.m.langley@gmail.com:skidoosh1','sabludau@gmail.com:dgbczusa1','edward_redko@hotmail.co.uk:1basketball','nkallio11@gmail.com:Steelers43','chicokablau@gmail.com:m7ecdi7j','rnh0925@gmail.com:cabezon06','malcolmpattern@gmail.com:reddwarf1','Gvdheijden01@hotmail.com:trampo123','victor19990315@me.com:Dewalt123','brenton_af@hotmail.com:surf1986','flippinj21@yahoo.com:skyblue2','rjgreaves@yahoo.co.uk:Manutd73','jeffkapelke32547@gmail.com:katia5299','dr.mad.01@mail.ru:maksimus2008','Mmanson702@yahoo.com:Lucas123','gustavosilvalima@hotmail.com:120392gu','tifok3@gmail.com:zxcvb213','th3ph4nt0mcarsteam@gmail.com:caca1234','CadienteJulian@gmail.com:Jjll0094','comodon14@gmail.com:Anakin14','iangarciaquerol@gmail.com:annaquerol1','colleen.propst@gmail.com:cooking123','alistair404@gmail.com:F15fighter','gustavandersson40@yahoo.com:Gretzky99']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Fortnite Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+spotify'):
        randomlist = ['Bryan13rs@hotmail.com:1311200050','Luktegod@gmail.com:rasa123123','Pandascansmosh@gmail.com:smosHy77','PokeMasterTroy10@yahoo.com:ttroja6123','adrianbarratt@yahoo.co.uk:ad1956tt','alanaguy@gmail.com:15year77','alexisgarcia1998@aol.com:jasper100','alexpw74@gmail.com:alessandr0','andrea_vinci1@hotmail.it:89NdrVnc','anne@lindemose.dk:anwo1705','armand.poupeau@laposte.net:armand12370','arnepeirs@hotmail.com:habbos007','boebelieter@gmail.com:Boebash88','chrisjungfleisch@me.com:aykahusky3425','christel.b@hotmail.ch:arnaud2312','christina030976@gmail.com:autumn5106','cirocaputo@hotmail.it:16091993','cooksrus5@sbcglobal.net:Shadow66','cristianaustin.ca@gmail.com:460Cristian','daamixtv@gmail.com:class123','danieltomczyk0@gmail.com:danielek1','drumminjohn@gmail.com:7e98vqj1','emylouzxc@hotmail.co.uk:Lauren01','eneddol@live.de:c85a3bz10','enesoyun190@gmail.com:tokmak19','fifi_30@hotmail.fr:phildu77','filipemacedo@outlook.com:fogofriu13','fisken_arne@hotmail.com:c9mnI3r6c','gauthmartin29@gmail.com:margauth','giafnafan@gmail.com:beary123','gregobarthez@hotmail.fr:olympien','haris2310@gmail.com:05sep2002','hellequin1989@gmail.com:digimon22','hisnik@list.ru:52267221','impact02.shok1812@hotmail.fr:shok1812','ismaeelfarook786@gmail.com:Bossy786','javierterrontorres@gmail.com:javier2400','jggconde@gmail.com:gold1986','jhp2000@hotmail.dk:pedersen13','jillrmt@hotmail.com:lhxyo69y','joshuapedrera@gmail.com:Cooloo11','jtkincaid11@gmail.com:Football11','julie.berder@gmail.com:pyramide','julioirui@hotmail.com:valencia','justine.cassi@hotmail.fr:Thesims2','kapa.96@live.it:antonio97','katmom@goowy.com:Gators107','kauan_batata@hotmail.com:pok7545689','kaziu.kazmierczak.23@wp.pl:kuba2502','kylehall876@hotmail.com:exkalibur1','laurent.chanel@orange.fr:adelaide1','leorodini@gmail.com:wowleo123','lilieetoile@hotmail.fr:chouchou','lng.jntn@gmail.com:dbxb1299943','lorythebest52@live.it:panino123','lsfuentes2@gmail.com:terapia123','lucidoptimist@gmail.com:Lineinsand46','luigi-scp94@hotmail.fr:30041983','m.c.hauenstein@gmail.com:2Aspen81611','m.denny@libero.it:franci','m3rkut@libero.it:191607mm','maddmartin@gmail.com:m2ko0l','maheswara.ramandana@gmail.com:maheswara03','marcoslptr@hotmail.com:nascar09','mariecompagnon4@gmail.com:corsica4','matiss0303@gmail.com:ezitis03','matthieu.l@free.fr:14120208','maxfdev@gmail.com:titire123','mazoru@live.fr:axel20','mbsolisg@gmail.com:Bebe1004','mesiaswael@gmail.com:waelzajel','micheleamoruso96@gmail.com:Trani96','nattawwat.j@gmail.com:0970605985','nflcrazy@yahoo.com:NFLcra2y','oasalazarleiva@yahoo.com.ar:oscar1969','omassillian@yahoo.fr:olimax1','ophelie-valayer@hotmail.fr:tournon98','pea_maxsimumcannon@hotmail.com:daebak19','projekt_mayhem@msn.com:nothing13','qualifac@yahoo.fr:philoria','rolof@web.de:geheim123','saawalkhn@googlemail.com:saawal123','saracostruzioni2@gmail.com:31011974','sarahbarlow21@yahoo.co.uk:gratten21','shannonwong92@hotmail.com:bing173174','si.ledda@live.it:pippo1998','silentundertaker96@gmail.com:Undertaker14','skomplikowany111@gmail.com:szynszyl123','sondrenr@gmail.com:Sondre12','ssj4darqueman@gmail.com:lita6969','swsolomon9@yahoo.com:Tarheels9','taiwo51@hotmail.fr:jujululu','techoffy@shaw.ca:V0nnifer','terrencetownsend1999@gmail.com:Mike1999','thomas@northerndarkness.org:Service58542','titeufdu27@hotmail.fr:3a1619b34','tobias.friesacher@gmail.com:peter4711','tristan.edelman17@gmail.com:Shark12356','tstahlecker2019@gmail.com:Texas2019','tyler.mudaliar@gmail.com:ghosttown1120','valentin.93@live.it:6aprile94','veenus66@aol.com:sweetv417','ventura.talamo@hotmail.it:gerardot','vitosimone01@att.net:8920Maple','wswatson@gmail.com:Whatsup63','xontor4400@gmail.com:codyb004','yogeshjuneja@gmail.com:yogi1234','yurif09@gmail.com:luasol123']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Spotify Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+stock'):
        await message.author.send("```Origin: 670 .Hulu: 421 .Spotify: 621 .Fortnite: 1000 .Nordvpn: 444 .Crunchyroll: 272 .Uplay: 300 .Minecraft: 441```")
        await message.author.send("```Available Stocks 26 October```")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")

    if message.content.startswith('+nordvpn'):
        randomlist = ['Nikkicornelius2003@yahoo.com:Craig12345','aaron.kienwald@gmail.com:Kienwald47','acsebar@gmail.com:trixie1s','alextaylor24@outlook.com:Tayloral2480','andyshops@gmail.com:355660av','batiss2012@hotmail.com:Lokero22','borisgr.od@gmail.com:7336406s','brant.g101@gmail.com:gra00145','bridougrus@gmail.com:BrianRussell1','canit19@gmail.com:knight19','carlghare2@gmail.com:740027924cgh','cassandra_flower@hotmail.com:Brijaxmad112827','cbilzx@tom.com:tmen0201','chantellemurphy@msn.com:qwerty55','clerbaek@gmail.com:Maria123','codyvugslol@gmail.com:Codyvugs99','cokeforyouu@gmail.com:adminben1','cole070500@gmail.com:trooper20','colehaynes99@gmail.com:clyde101','colmasimone@gmail.com:left4dead2','cr8tion21@gmail.com:deriando0','craftmattpll@gmail.com:matiziomek123','creepercraft19@gmail.com:tomtom123','daibi1998@gmail.com:0988956586','danielgalo6@gmail.com:minhasenha123','dayz101airborne@gmail.com:Ghost123','dcl@jettisonnetworks.com:62562DcL','delaunayalexandre18@gmail.com:Alexandre9','denis.abazovic@gmail.com:redrose88','dizbfe7h@gmail.com:dizbfe7h','djones0305@gmail.com:shpoople68','djtallar@gmail.com:pwwoozle','donramon2005@yahoo.com:snoopy2006','dpdowd@att.net:dpdljad23','drsnh2000@gmail.com:mummy123','dyamondz@hotmail.com:habiba24','emily_hercamp@hotmail.com:withlove1','eric@ericproffitt.com:beun2you','fabiangol16@gmail.com:matrix11','federicomariani215@gmail.com:Camilla78','flytouk@gmail.com:19831017','gw_mythic@hotmail.com:25979561','harveydawe9@gmail.com:dododog01','helenasotto@gmail.com:trustNO1','hunghung5629@gmail.com:bluethunder','info@kaeshammer.com:gonzorascal','jessie.ceyssens@telenet.be:yorkoo101171','jorv101@icloud.com:qazedc11','killerburrito.aj@gmail.com:Awesome01','klaudivarius@gmail.com:fcporto22','kojjawabakulu@gmail.com:kaggwalove','kyle.voorhees01@gmail.com:Voorhees1','laloantoniocercadovera@hotmail.com:1997LAlo','larsxthomsen@gmail.com:ims0c00l','lhl_aus@hotmail.com:honda3724','lukasluby69@gmail.com:saradomin756','m_odonnell_08@hotmail.co.uk:2588buff','madianne22@outlook.com:Roxybuster09','maksnovikoff@gmail.com:1488maxim','malin_westin@hotmail.com:billytorres','marcciupan@gmail.com:09165303600','marcus.ovhed@hotmail.com:Sani2579','marinushove@hotmail.com:Kasperkat20','markgregg87@gmail.com:ddrwars87','maroc77@msn.com:Hayat1710','masterhung15@gmail.com:Ethanx15','max.1029@icloud.com:Max102903','mcook@scattergood.org:Indianapolis','medievil757@hotmail.com:Smithy200010','mikevance101392@gmail.com:4marijuana','mmineweaser@gmail.com:dragon99','mrdearman@hotmail.com:Hondacrv58','mshinkle28462@gmail.com:Sassyfras1','multikillerdiamant@gmail.com:2130mkmk','nick.chen053100@gmail.com:Greatwall1','pachurick@hotmail.com:darkzero22','party_animal92@hotmail.co.uk:florida06','princessrravenaa@hotmail.com:ruthralingam28','princetarun4u@gmail.com:feelmylove','ra.boogie@gmail.com:carter15','rbcasselberry@yahoo.com:Tanner85','redclus@gmail.com:Gilang1409','redgerton89@gmail.com:Jordan08','rozhokserega@gmail.com:12qwaszx','sammclaren123@gmail.com:qwe10443','samsanai78@gmail.com:blackhawks99','sanchezfranklin005@gmail.com:Jamuel1205','sandmangritz1@hotmail.com:mrgritz1','scot106@gmail.com:bayshore98','sigurdlykke7@gmail.com:Sigurd12','spence77@live.co.uk:Saskia55','stevenzuo@me.com:ztddwo1992','tanneraustin14@gmail.com:pepper123','tanyakennedy99@gmail.com:p1an0f0rte','tommygorman1@aol.com:roisin2612','tsherman219@gmail.com:tristan123','vincent.f.delatorre@gmail.com:cheeseee1','vishalbijlani@gmail.com:vishal1975','wakeboarding315@gmail.com:cr03151993','xbones123@hotmail.com:nikolai55','zachosowski@yahoo.com:Pissman123','zorgish@hotmail.com:Tissekatt1','zuber678@yahoo.com:23212321']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" Official Server https://discord.gg/44PFcRr ")
        msg = ' ' + author + '. Nord Vpn Account : '
        await message.author.send(msg + (random.choice(randomlist)))



    if message.content.startswith('+origin'):
        randomlist = ['asianpwnage@yahoo.com:megaman28','chris.gravenmier@yahoo.com:9449295a','jayden3221@yahoo.com:penguin77','thimodejonge@hotmail.com:Killer33','Brandon.Allin@yahoo.com:357Bolter','Josephjones2014@hotmail.com:Mookie08','ajringor@rocketmail.com:pogiako22','alecwbaugher@gmail.com:Masseffect3','alex.boswell87@gmail.com:Alexeb87','alexanderdevlin@yahoo.com:MKaasr12','allyblacksinger@gmail.com:greenbowAL123','anh11_fox@yahoo.com:flyingfoxx11','asianpwnage@yahoo.com:megaman28','badcreeper58@gmail.com:1556431113','bfrench1999@gmail.com:Branden99','chris.gravenmier@yahoo.com:9449295a','colejr3@comcast.net:Pickle00','crazyboydiamond@gmail.com:yahoo123','djunknow@wp.pl:tomek1988','dragons1182@gmail.com:muppet11','eracsgod@gmail.com:ferrum26','espartan208@hotmail.com:halowars11','falcon5840@yahoo.com:67Corvette','hunttheer@gmail.com:Hunter27','iuzaru@yahoo.com:zxcvbn98','jaja808@wp.pl:kometa666','jayden3221@yahoo.com:penguin77','jensa96@hotmail.com:C3oNimaH','jordanxchang@yahoo.com:Abcde123','juozaskarciauskas@gmail.com:hesoyam','madmadammoll@yahoo.com:Molly0826','marauder6307@yahoo.com:Ringwraith3321','marlisasikkema@outlook.com:Krabeltje1','mikicom11@gmail.com:mikit6266','momluvsglass@ymail.com:Lucky1967','mstsant@yahoo.com:Fs841110','natemcginnis29@gmail.com:Godawgs1','rie.nateriver@gmail.com:mamake92','sepulvedam90@yahoo.com:cowboys24','shane.henniger@yahoo.com:Isaac100','simon36123@yahoo.com:12345678As','slmtrm@charter.net:Excalibur1','szadowk2000@wp.pl:Animelike2000','tazzydevil2002@live.com:monkeyboyabc123','trieuvan171@gmail.com:171993771','vacus619@yahoo.com:volleyforged','w.beer208@gmx.de:ChefSache1','waynet3ch@gmail.com:Cowboy19']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Origin Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+hulu'):
        randomlist = ['Haymae11@yahoo.com:Missme27','acex8781@gmail.com:Dragones6','alec.olen@yahoo.com:1Tennisfreak','alondra-acosta@hotmail.com:22happy22','andrei.sel.12@gmail.com:Andrew2503','anonymousdude666@gmail.com:momdad','azarmir.kasra@gmail.com:4008086q','b.aguilar34@yahoo.com:Acura2004','ben.reeves@gmail.com:skull9062','cam.williams0824@gmail.com:Cameron098','catguitarist@hotmail.co.uk:Dr34dw1ng','cesar.a.vieira@hotmail.com:forever3390','cuellarrico@yahoo.com:Yelitza7','cvmissy16@gmail.com:sweets2','daniel_jared@live.com:frida2011','dantealhigeri@hotmail.com:liukan15','desireianngalgana@hotmail.com:galgana1','dibl_96@hotmail.com:Diblteam06','dillonrockson@gmail.com:shaggy66','dino.duel@hotmail.com:Killer123','does_molly_ring_a_bell@yahoo.com:Jetaime23','ecchizz@live.com:seay15','elanning@gmail.com:althain2k9','esa0705@gmail.com:natsudragneel123','fireworks125machinima@gmail.com:poopoo10','gerard_liwanag@hotmail.com:Boxing101','glztiger@hotmail.it:somuas35','grimreaper0x0@yahoo.com:darkblade99','guigui2397@gmail.com:doudou98','hellscream0@hotmail.com:cotton99','henrikyo_inteligente@hotmail.com:99585849','imdewidesigns@gmail.com:Memelose1','isabelcalle_17@hotmail.com:kurosagi21','jiiub@hotmail.com:sebhan89','jmholohan@hotmail.com:Cc6260368','jnguyen5151@yahoo.com:bobby5151','jose15tito@msn.com:champ247','jroxendine@rocketmail.com:rxw420','jstanton14@hotmail.com:netx4984','kokiks101@gmail.com:shadow12','lastshogun@gmail.com:moses100','ldavis4127@aol.com:bingo222','leep.egerton@ntlworld.com:Abigail1','mapcra500@live.com:destroyer1','marcelocdomingues@hotmail.com:d11m5a71','marci690@gmail.com:risiko123','mattspvfx@gmail.com:power544','mauro_852@hotmail.com:marc1993','mdlmx19@gmail.com:xpootanX18','mikerob175@gmail.com:canes175','mykiddani@yahoo.com:bobby5689','naderpug@gmail.com:soarer','nekoiv9@gmail.com:aaaaaakiba04','nicholasmireles@yahoo.com:nick1998','nsjames7000@gmail.com:poopster2','ongteckwei@yahoo.com:keropi','pablo.asin@hotmail.es:barrancas1','pieguy798@gmail.com:HONDARIDER98','pirateking_nick@yahoo.com:my2ndname2','ptvheather@gmail.com:sept22000','quinnfoley@gmail.com:bears2012','rafaelflorers@yahoo.com:clubyes09','rezafatul@yahoo.co.id:moskwa','rodri9044@hotmail.com:huehue123','rodrigo.neta@gmail.com:lego541998','rolandcmorales08@gmail.com:000black','savualexandru0@gmail.com:ronaldo99','shinigmainox@gmail.com:miniwiflyXD1','shizzy186@yahoo.com:Warlover101','simen@vetaas-hoie.com:12Oktober','slipknot_dark1496@hotmail.com:presario14','speightquantez@gmail.com:speight1','sphireos@gmail.com:thailson1','steam21@vp.pl:Aezakmi12','steven.hellingh@gmail.com:3A55word','subtil.guilherme@gmail.com:rock4ever','t.ingh@live.nl:WIIkey25','themathwhizo@gmail.com:Mathpro2013','timmy_cattan@hotmail.com:Electrical1','travis.ber@gmail.com:Polpol123','vajsteve@gmail.com:thug4life','vigotheyt@gmail.com:pirate11','vijyaraj@gmail.com:rajmahal25','wbluke7000@gmail.com:moses711','westell626@gmail.com:godofwar','zach.ricketts@gmail.com:Smith230']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Hulu Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+steam'):
        randomlist = ['https://filemedia.net/27527/steam	','https://filemedia.net/27527/steam	','https://filemedia.net/27527/steam	']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Steam Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+udemy'):
        randomlist = ['https://filemedia.net/27527/udemy2','https://up-to-down.net/27527/udemy','https://up-to-down.net/27527/udemy']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+uplay'):
        randomlist = ['https://up-to-down.net/27527/uplay2','https://up-to-down.net/27527/uplay2','https://up-to-down.net/27527/uplay']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Uplay Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+crunchyroll'):
        randomlist = ['https://up-to-down.net/27527/crunchyroll','https://up-to-down.net/27527/crunchyroll','https://up-to-down.net/27527/crunchyroll']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Crunchyroll Account : '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+scribd'):
        randomlist = ['https://direct-link.net/27527/Scribd','https://direct-link.net/27527/Scribd','https://direct-link.net/27527/Scribd']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+familyowner'):
        randomlist = ['https://direct-link.net/27527/familyowner','https://direct-link.net/27527/familyowner','https://direct-link.net/27527/familyowner']
        msg = 'Hello ' + author + '. Your link: '
        await message.author.send(msg + (random.choice(randomlist)))

    if message.content.startswith('+minecraft'):
        randomlist = ['https://link-to.net/27527/Minecraft001','https://up-to-down.net/27527/minecrafts','https://filemedia.net/27527/Minecraft']
        await message.author.send("Join Server To Keep Updated About Bot")
        await message.author.send(" https://discord.gg/sZpqqWX ")
        msg = ' ' + author + '. Minecraft Account : '
        await message.author.send(msg + (random.choice(randomlist)))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    change_status.start()

@tasks.loop(seconds=5)
async def change_status():
        await client.change_presence(activity=Activity(name=f"{len(client.guilds)} servers!| +help | Members ", 
                                                type=ActivityType.watching))

client.run(os.getenv('BOT_TOKEN'))
