import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime 
def removeAccents(input_text):

    strange = 'ŮôῡΒძěἊἦëĐᾇόἶἧзвŅῑἼźἓŉἐÿἈΌἢὶЁϋυŕŽŎŃğûλВὦėἜŤŨîᾪĝžἙâᾣÚκὔჯᾏᾢĠфĞὝŲŊŁČῐЙῤŌὭŏყἀхῦЧĎὍОуνἱῺèᾒῘᾘὨШūლἚύсÁóĒἍŷöὄЗὤἥბĔõὅῥŋБщἝξĢюᾫაπჟῸდΓÕűřἅгἰშΨńģὌΥÒᾬÏἴქὀῖὣᾙῶŠὟὁἵÖἕΕῨčᾈķЭτἻůᾕἫжΩᾶŇᾁἣჩαἄἹΖеУŹἃἠᾞåᾄГΠКíōĪὮϊὂᾱიżŦИὙἮὖÛĮἳφᾖἋΎΰῩŚἷРῈĲἁéὃσňİΙῠΚĸὛΪᾝᾯψÄᾭêὠÀღЫĩĈμΆᾌἨÑἑïოĵÃŒŸζჭᾼőΣŻçųøΤΑËņĭῙŘАдὗპŰἤცᾓήἯΐÎეὊὼΘЖᾜὢĚἩħĂыῳὧďТΗἺĬὰὡὬὫÇЩᾧñῢĻᾅÆßшδòÂчῌᾃΉᾑΦÍīМƒÜἒĴἿťᾴĶÊΊȘῃΟúχΔὋŴćŔῴῆЦЮΝΛῪŢὯнῬũãáἽĕᾗნᾳἆᾥйᾡὒსᾎĆрĀüСὕÅýფᾺῲšŵкἎἇὑЛვёἂΏθĘэᾋΧĉᾐĤὐὴιăąäὺÈФĺῇἘſგŜæῼῄĊἏØÉПяწДĿᾮἭĜХῂᾦωთĦлðὩზკίᾂᾆἪпἸиᾠώᾀŪāоÙἉἾρаđἌΞļÔβĖÝᾔĨНŀęᾤÓцЕĽŞὈÞუтΈέıàᾍἛśìŶŬȚĳῧῊᾟάεŖᾨᾉςΡმᾊᾸįᾚὥηᾛġÐὓłγľмþᾹἲἔбċῗჰხοἬŗŐἡὲῷῚΫŭᾩὸùᾷĹēრЯĄὉὪῒᾲΜᾰÌœĥტ'

    ascii_replacements = 'UoyBdeAieDaoiiZVNiIzeneyAOiiEyyrZONgulVoeETUiOgzEaoUkyjAoGFGYUNLCiIrOOoqaKyCDOOUniOeiIIOSulEySAoEAyooZoibEoornBSEkGYOapzOdGOuraGisPngOYOOIikoioIoSYoiOeEYcAkEtIuiIZOaNaicaaIZEUZaiIaaGPKioIOioaizTIYIyUIifiAYyYSiREIaeosnIIyKkYIIOpAOeoAgYiCmAAINeiojAOYzcAoSZcuoTAEniIRADypUitiiIiIeOoTZIoEIhAYoodTIIIaoOOCSonyKaAsSdoACIaIiFIiMfUeJItaKEISiOuxDOWcRoiTYNLYTONRuaaIeinaaoIoysACRAuSyAypAoswKAayLvEaOtEEAXciHyiiaaayEFliEsgSaOiCAOEPYtDKOIGKiootHLdOzkiaaIPIIooaUaOUAIrAdAKlObEYiINleoOTEKSOTuTEeiaAEsiYUTiyIIaeROAsRmAAiIoiIgDylglMtAieBcihkoIrOieoIYuOouaKerYAOOiaMaIoht'

    translator = str.maketrans(strange, ascii_replacements)

    return input_text.translate(translator)
    
def NADUVI_to_XML(df,j0,i):
    df["DATA_OPERACJI"].astype('datetime64')
    df["DATA_WYSTAWIENIA"].astype('datetime64')
    ROOT = ET.Element("ROOT", **{"xmlns":"http://www.cdn.com.pl/optima/dokument"})
    DOKUMENT = ET.SubElement(ROOT,"DOKUMENT")
    NAGLOWEK = ET.SubElement(DOKUMENT,"NAGLOWEK")
    #NAGŁOWEK
    GENERATOR = ET.SubElement(NAGLOWEK,"GENERATOR")
    GENERATOR.text = "Comarch Opt!ma"
    TYP_DOKUMENTU = ET.SubElement(NAGLOWEK,"TYP_DOKUMENTU")
    TYP_DOKUMENTU.text = "308"
    #DATA_WYSTAWIENIA
    DATA_WYSTAWIENIA = ET.SubElement(NAGLOWEK,"DATA_WYSTAWIENIA")

    DATA_WYSTAWIENIA.text = str(df.loc[j0,"DATA_WYSTAWIENIA"]).replace(" 00:00:00","")

    DATA_OPERACJI = ET.SubElement(NAGLOWEK,"DATA_OPERACJI")

    DATA_OPERACJI.text = str(df.loc[j0,"DATA_OPERACJI"]).replace(" 00:00:00","")
    
    OPIS = ET.SubElement(NAGLOWEK,"OPIS")
    OPIS.text = str(df.loc[j0,"DESCRIPTION"])
    #PLATNIK
    PLATNIK = ET.SubElement(NAGLOWEK,"PLATNIK")
    KOD = ET.SubElement(PLATNIK,"KOD")
    KOD.text = "NADUVI.NL"
    #/PLATNIK
    #ODBIORCA
    ODBIORCA = ET.SubElement(NAGLOWEK,"ODBIORCA")
    KOD = ET.SubElement(ODBIORCA,"KOD")
    KOD.text = str(df.loc[j0,"RECIPIENT_NAME"])
    NIP_KRAJ = ET.SubElement(ODBIORCA,"NIP_KRAJ")
    NIP_KRAJ.text = str(df.loc[j0,"RECIPIENT_COUNTRY_NIP"])

    NIP = ET.SubElement(ODBIORCA,"NIP")
    if  df.loc[j0,"RECIPIENT_NIP"]== df.loc[j0,"RECIPIENT_NIP"]:
        NIP.text = str(df.loc[j0,"RECIPIENT_NIP"])
    
    NAZWA = ET.SubElement(ODBIORCA,"NAZWA")
    NAZWA.text =removeAccents(str(df.loc[j0,"RECIPIENT_NAME"]))
    #ADRES ODBIORCA
    ADRES = ET.SubElement(ODBIORCA,"ADRES")
    
    ULICA = ET.SubElement(ADRES,"ULICA")
    ULICA.text = removeAccents(str(df.loc[j0,"RECIPIENT_STREET"]))
    
    KOD_POCZTOWY = ET.SubElement(ADRES,"KOD_POCZTOWY")
    KOD_POCZTOWY.text = str(df.loc[j0,"RECIPIENT_POSTAL_CODE"])

    MIASTO = ET.SubElement(ADRES,"MIASTO")
    MIASTO.text = removeAccents(str(df.loc[j0,"RECIPIENT_CITY"]))

    KRAJ = ET.SubElement(ADRES,"KRAJ")
    if NIP_KRAJ.text=="DE":
        KRAJ.text = "GERMANY"
    elif NIP_KRAJ.text=="NL":
        KRAJ.text = "NEATHERLAND"
    elif NIP_KRAJ.text=="BE":   
        KRAJ.text = "BELGIUM"

    #/ADRES ODBIORCA
    #/ODBIORCA
    WALUTA = ET.SubElement(NAGLOWEK,"WALUTA")
    SYMBOL = ET.SubElement(WALUTA,"SYMBOL")
    SYMBOL.text = "EUR"
    MAGAZYN_ZRODLOWY = ET.SubElement(NAGLOWEK,"MAGAZYN_ZRODLOWY")
    MAGAZYN_ZRODLOWY.text = str(df.loc[j0,"WAREHOUSE"])

    POZYCJE = ET.SubElement(DOKUMENT,"POZYCJE")

    ATRYBUTY = ET.SubElement(DOKUMENT,"ATRYBUTY")
    ATRYBUT_TELEPHONE = ET.SubElement(ATRYBUTY,"ATRYBUT")
    KOD = ET.SubElement(ATRYBUT_TELEPHONE,"KOD")
    KOD.text = "TELEPHONE"
    WARTOSC = ET.SubElement(ATRYBUT_TELEPHONE,"WARTOSC")
    if  df.loc[j0,"RECIPIENT_PHONE"]==df.loc[j0,"RECIPIENT_PHONE"]:
        WARTOSC.text = str(df.loc[j0,"RECIPIENT_PHONE"])

    ATRYBUT_ADDITIONAL = ET.SubElement(ATRYBUTY,"ATRYBUT")
    KOD = ET.SubElement(ATRYBUT_ADDITIONAL,"KOD")
    KOD.text = "ADDITIONAL"
    WARTOSC = ET.SubElement(ATRYBUT_ADDITIONAL,"WARTOSC")
    if  df.loc[j0,"RECIPIENT_ADDITIONAL"]==df.loc[j0,"RECIPIENT_ADDITIONAL"]:
        WARTOSC.text = removeAccents(str(df.loc[j0,"RECIPIENT_ADDITIONAL"]))

    ATRYBUT_MAIL = ET.SubElement(ATRYBUTY,"ATRYBUT")
    KOD = ET.SubElement(ATRYBUT_MAIL,"KOD")
    
    KOD.text = "MAIL"
    WARTOSC = ET.SubElement(ATRYBUT_MAIL,"WARTOSC")
    if  df.loc[j0,"RECIPIENT_EMAIL"]==df.loc[j0,"RECIPIENT_EMAIL"]:
        WARTOSC.text = str(df.loc[j0,"RECIPIENT_EMAIL"])

    for j in df[df["No."]==i].index:
        POZYCJA = ET.SubElement(POZYCJE,"POZYCJA")
        LP = ET.SubElement(POZYCJA,"LP")
        LP.text = str(df.loc[j,"LP"])
        TOWAR = ET.SubElement(POZYCJA,"TOWAR")
        KOD = ET.SubElement(TOWAR,"KOD")
        KOD.text = str(df.loc[j,"REFERENCE"])
        WALUTA = ET.SubElement(POZYCJA,"WALUTA")
        SYMBOL = ET.SubElement(WALUTA,"SYMBOL")
        SYMBOL.text = "EUR"
        WARTOSC_NETTO_WAL = ET.SubElement(POZYCJA,"WARTOSC_NETTO_WAL")
        WARTOSC_NETTO_WAL.text = str(df.loc[j,"COST"])
        ILOSC = ET.SubElement(POZYCJA,"ILOSC")
        ILOSC.text = str(df.loc[j,"QUANTITY"])

    return(ET.tostring(ROOT, encoding='unicode', method='xml'))

def NADUVI_csv_to_check_xlsx(df_NADUVI):
    df_NADUVI = df_NADUVI[["Order reference","Date","Full name","Phone","Email","Address line 1","City","Postcode","Country","SKU","Quantity"]] 
    count = 1
    for i in df_NADUVI["Order reference"].unique():
        for j in df_NADUVI[df_NADUVI["Order reference"]==i].index:
            df_NADUVI.loc[j,"No."] = count
        count = count + 1
    df1=pd.DataFrame()
    df1["No."] = df_NADUVI["No."]
    df1["DESCRIPTION"] = "NADUVI_" + df_NADUVI["Country"] + "_"+df_NADUVI["Order reference"]
    df1["WAREHOUSE"] = "MAGAZYN"
    df1["DATA_OPERACJI"] = datetime.date(datetime.now()).strftime("%Y-%m-%d")
    df1["DATA_WYSTAWIENIA"] = ""
    df1["RECIPIENT_CODE"] = df_NADUVI["Full name"]
    df1["RECIPIENT_NAME"] = df_NADUVI["Full name"]
    df1["RECIPIENT_STREET"]	= df_NADUVI["Address line 1"].str.replace(" ","_")
    df1["RECIPIENT_CITY"] = df_NADUVI["City"]
    df1["RECIPIENT_POSTAL_CODE"]= df_NADUVI["Postcode"]
    df1["RECIPIENT_COUNTRY_NIP"]= df_NADUVI["Country"]
    df1["RECIPIENT_NIP"]= ""
    # df1["RECIPIENT_NIP"]
    df1["RECIPIENT_PHONE"]	= df_NADUVI["Phone"]
    df1["RECIPIENT_EMAIL"]	= df_NADUVI["Email"]
    df1["RECIPIENT_ADDITIONAL"]= ""
    df1["LP"] = ""
    df1["REFERENCE"] = df_NADUVI["SKU"].str.replace("BESO-","")
    df1["COST"] = ""
    df1["QUANTITY"] = df_NADUVI["Quantity"]
    for i in df1["No."].unique():
        count = 1
        for j in df1[df1["No."]==i].index:
            df1.loc[j,"LP"] = count
            count = count + 1
            if len(df1.loc[j,"RECIPIENT_STREET"])>40:
                street=df1.loc[j,"RECIPIENT_STREET"]
                df1.loc[j,"RECIPIENT_STREET"] = street[:40]
                df1.loc[j,"RECIPIENT_ADDITIONAL"] = street[-len(street)+40:]

    # colors = ['gold', 'lightblue','lightgreen','limegreen','pink']
    # x = df1.copy()
    # # factors = list(x['CAR'].unique())
    # # i = 0
    # # for factor in factors:
    # #     style = f'background-color: {colors[i]}'
    # #     x.loc[x['CAR'] == factor, :] = style
    # #     i = not i


    # factors = x.columns
    # i = 0
    # for factor in factors:
    #     if factor == "DATA_WYSTAWIENIA" or factor == "WAREHOUSE" or factor == "COST":
    #         x.loc[:, factor] =f'background-color: {colors[4]}'



    # df1=df1.style.apply(x, axis=None)
    return df1