odp_pop = []
odp_num = []
pyt_num = 0
przyt = slice(1, -1)

# pyt("tutaj piszesz pytanie", "odpowiedź A", "odpowiedź B", "odpowiedź C", "odpowiedź D", "poprawna odpowiedź do pytania (A,B,C,D)")


def pyt(pytanie, odp_a, odp_b, odp_c, odp_d, poprawne):
    global pyt_num
    pyt_num += 1
    print('<div class="question">'+str(pyt_num)+". "+pytanie[przyt]+'</div>')
    print('  <div class="answer" data-answer="A" onclick="selectAnswer(this, \'A\', '+str(pyt_num)+')">A. '+odp_a[przyt]+'</div>')
    print('  <div class="answer" data-answer="B" onclick="selectAnswer(this, \'B\', '+str(pyt_num)+')">B. '+odp_b[przyt]+'</div>')
    print('  <div class="answer" data-answer="C" onclick="selectAnswer(this, \'C\', '+str(pyt_num)+')">C. '+odp_c[przyt]+'</div>')
    print('  <div class="answer" data-answer="D" onclick="selectAnswer(this, \'D\', '+str(pyt_num)+')">D. '+odp_d[przyt]+'</div>')
    odp_pop.append(poprawne.upper()[przyt])
    odp_num.append(pyt_num)
    print()


# pyt(" Monitor CRT łączy się z kartą graficzną za pomocą złącza ", " D-USB ", " D-SUB ", "  BNC ", "  PCMCIA ", " B ")
# pyt(" Na wydrukach drukarki laserowej można zaobserwować podłużne pasma oraz powtarzające się artefakty. Możliwą przyczyną złej jakości wydruku jest usterka ", " głowicy drukującej ", " układu zliczającego ", " bębna światłoczułego ", " taśmy barwiącej. ", " C ")
# pyt(" Który protokół działa w warstwie aplikacji modelu ISO/OSI umożliwiając wymianę informacji kontrolnych pomiędzy urządzeniami sieciowymi? ", " DNS ", " SNMP ", " POP3", " SMTP ", " B ")
# pyt(" Ile podwójnych gniazd RJ45 powinno być zamontowanych w pomieszczeniu o wymiarach 8 x 5 m, aby były spełnione zalecenia normy PN-EN 50173? ", "10 gniazd ", "8 gniazd ", "5 gniazd ", "4 gniazda ", " D ")
# pyt(" Zgodnie z normą TIA/EIA-568-B.1 kabel UTP 5e z przeplotem jest tworzony poprzez zamianę ułożenia we wtyczce 8P8C następujących par przewodów (odpowiednio według kolorów): ", " biało-zielony i zielony z biało-niebieskim i niebieskim ", " biało-pomarańczowy i pomarańczowy z biało-brązowym i brązowym ", " biało-pomarańczowy i pomarańczowy z biało-zielonym i zielonym ", " biało-zielony i zielony z biało-brązowym i brązowym ", " C ")
# pyt(" Administrator zauważył, że w sieci LAN występuje duża liczba kolizji. Które urządzenie powinien zainstalować, aby podzielić sieć lokalną na mniejszy domeny kolizji? ", " Przełącznik ", " Modem ", " Router ", " Koncentrator ", " A ")
# pyt(" Typowym objawem wskazującym na zbliżającą się awarię dysku twardego jest pojawienie się ", " komunikatu CMOS checksum error ", " komunikatu Diskette drive A error ", " błędów zapisu i odczytu dysku ", " trzech krótkich sygnałów dźwiękowych ", " C ")
# pyt(" CommView i WireShark to programy stosowane do ", " zabezpieczenia transmisji danych w sieci ", " sprawdzania zasięgu sieci bezprzewodowej ", " analizowania pakietów transmitowanych w sieci ", " określania wielkości tłumienia w torze transmisyjnym ", " C ")
# pyt(" Które określenie dotyczące konta użytkownika Active Directory w systemie Windows jest prawdziwe? ", " Nazwa logowania użytkownika może mieć długość większą niż 100 bajtów ", " Nazwa logowanie użytkownika nie może mieć długości większej niż 100 bajtów ", " Nazwa logowania użytkownika musi mieć mniej niż 21 znaków ", " Nazwa logowania użytkownika musi mieć mniej niż 20 znaków ", " A ")
# pyt(" Jaki protokół służy do translacji pomiędzy publicznymi i prywatnymi adresami IP? ", " RARP ", " NAT ", " SNMP ", " ARP ", " B ")
# pyt(" Drugi monitor CRT podłączony do zestawu komputerowego służy do ", " wyprowadzania informacji ", " przetwarzania danych ", " kalibracji danych ", " przechowywania informacji ", " A ")
# pyt(" Najczęściej stosowany kodek mowy podczas konfiguracji bramki VoIP to ", " G.711", " AC3", " A.512", " GSM ", " A ")
# pyt(" Aby zwiększyć wydajność komputera w grach, karta graficzna Sapphire Radeon R9 FURY OC, 4GB HBM (4096 Bit), HDMI, DVI, 3xDP została wyposażona w technologię ", " Stream ", " CUDA ", " CrossFireX ", " SLI ", " C ")
# pyt(" Aby sprawdzić adres fizyczny karty sieciowej, w wierszu poleceń systemu operacyjnego Microsoft Windows należy wpisać polecenie ", " ipconfig /all ", " show mac ", " get mac ", " ifconfig -a ", " A ")
# pyt(" Który z protokołów jest protokołem synchronizacji czasu? ", " FTP ", " HTTP ", " NNTP ", " NTP ", " D ")
# pyt(' W czasie przeprowadzania procedury POST na ekranie pojawia się komunikat "CMOS Battery State Low". Co w takiej sytuacji należy zrobić, aby komunikat nie pojawił się w przyszłości ', " Podłączyć zasilanie sieciowe ", " Ustawić poprawnie opcje konfiguracyjne CMOS dotyczące zasilania ", " Wymienić baterię na płycie głównej komputera ", " Wymienić akumulatory laptopa na nowe ", " C ")
# pyt(" Powodem niekontrolowanego zapełnienia dysku może być ", " zbyt małe jednostki alokacji plików ", " wirus komputerowy ", " częsta defragmentacja ", " źle skonfigurowana pamięć wirtualna ", " B ")
# pyt(" W systemie Linux program fsck pozwala na ", " zlokalizowanie i naprawę uszkodzonych sektorów na dysku twardym ", " monitorowanie stanu procesora ", " usuwanie błędnych wpisów w rejestrze systemowym ", " testowanie wydajności karty sieciowej ", " A ")
# pyt(" Za pomocą którego polecenia systemu Linux możliwa jest zmiana domyślnej powłoki użytkownika egzamin na sh ", " usermod -s /bin/sh egzamin ", " groupmod /users/egzamin /bin/sh ", " vi /etc/passwd -sh egzamin ", " chmod egzamin /etc/shadow sh ", " A ")
# pyt(" Adres IP komputera wyrażony sekwencją 172.16.0.1 jest zapisany w systemie ", " szesnastkowym ", " dwójkowym ", " dziesiętnym ", " ósemkowym ", " C ")
# pyt(" Do wykonania kopii danych na dysk USB w systemie Linux stosuje się polecenie  ", " mv ", " cp ", " su ", " su ", " B ")
# pyt(" Urządzeniem, które służy do wycinania kształtów oraz grawerowania między innymi w materiałach drewnianych, szklanych i metalowych, jest ploter ", " bębnowy ", " olwentowy ", " laserowy ", " tnący ", " C ")
# pyt(" Zgodnie z normą PN-EN 50174 maksymalna długość przebiegu kabla poziomego kategorii 6 pomiędzy punktem abonenckim a punktem dystrybucyjnym w panelu krosowym wynosi  ", "90 m ", "110 m ", "100 m ", "150 m ", " A ")
# pyt(" Zdalne uwierzytelnianie użytkowników w sieciach bezprzewodowych może odbywać się za pomocą usługi  ", " HTTPS ", " IMAP ", " NNTP ", " RADIUS ", " D ")
# pyt(" Tusz żelowy jest stosowany w drukarkach – sublimacyjnych ", " sublimacyjnych ", " termotransferowych ", " igłowych ", " fiskalnych ", " A ")
# pyt(" Jaką nazwę nosi identyfikator, który musi być identyczny, aby urządzenia sieciowe mogły pracować w danej sieci bezprzewodowej? ", " IP ", " MAC ", " SSID ", " URL ", " C ")
# pyt(" ACPI jest skrótem oznaczającym ", " zaawansowany interfejs zarządzania konfiguracją i energią ", " zestaw ścieżek łączących jednocześnie kilka komponentów z możliwością komunikacji ", " program umożliwiający odnalezienie rekordu rozruchowego systemu ", " test poprawności działania podstawowych podzespołów ", " A ")
# pyt(" Ustawa z dnia 14 grudnia 2012 r. o odpadach nakazuje ", " neutralizację odpadów w dowolny sposób w jak najkrótszym czasie ", " spalenie odpadów w jak najwyższej temperaturze ", " składowanie odpadów maksymalnie przez 1 rok ", " poddanie odpadów w pierwszej kolejności odzyskowi ", " D ")
# pyt(" Protokół pocztowy, za pomocą którego możemy odbierać pocztę z serwera, to ", " FTP ", " POP3 ", " HTTP ", " SMTP ", " B ")
# pyt(" Liczba 45(H) zapisana w systemie ósemkowym ma postać ", "102 ", "108 ", "105 ", "110 ", " C ")
pyt(" Procesory CISC charakteryzują się ", " niewielką liczbą trybów adresowania ", " dużą liczbą rozkazów ", " ograniczaną komunikacją pomiędzy pamięcią a procesorem ", " prostą i szybką jednostką sterującą ", " B ")
pyt(" Użytkownik drukarki samodzielnie i prawidłowo napełnił pojemnik z tonerem. Po jego zamontowaniu drukarka nie podejmuje próby drukowania. Przyczyną tej usterki może być ", " zabrudzony wałek magnetyczny ", " zła jakość wykorzystanego tonera do uzupełnienia pojemnika ", " źle dobrany toner ", " niewymieniony chip zliczający, znajdujący się na pojemniku z tonerem ", " D ")
pyt(" Który standard specyfikacji IEEE 802.3 należy zastosować w środowisku, w którym występują zakłócenia elektromagnetyczne, jeśli odległość od punktu dystrybucyjnego do punktu abonenckiego wynosi 200 m? ", "100BaseFX ", "1000BaseTX ", "10Base2 ", "100BaseT ", " A ")
pyt(" Poleceniem służącym do aktualizowania systemu operacyjnego Linux z bazami RPM jest ", " upgrade ", " zypper ", " nm ", " chmode ", " B ")
pyt(" Które elementy systemu komputerowego podlegają utylizacji w wyspecjalizowanych zakładach przetwarzania z uwagi na zawartość niebezpiecznych substancji lub pierwiastków chemicznych? ", " Radiatory ", " Przewody ", " Obudowy komputerów ", " Tonery ", " D ")
pyt(" Użytkownik chce tak zmodernizować komputer, aby działały na nim gry wymagające DirectX12. Jaki system operacyjny powinien zakupić do modernizowanego komputera, aby wspierał DX12? ", " Windows 8 ", " Windows 8.1 ", " Windows 10 ", " Windows XP ", " C ")
pyt(" Złącze szeregowe na płycie głównej, służące do podłączania kart rozszerzeń o różnej, w zależności od wariantu, liczbie pinów nosi nazwę ", " PCI ", " AGP ", " ISA ", " PCI Express ", " D ")
pyt(" System S.M.A.R.T przeznaczony jest do monitorowania pracy i wykrywania błędów ", " napędów płyt CD/DVD ", " dysków twardych ", " płyty głównej ", " kart rozszerzeń ", " B ")
pyt(' Przy uruchamianiu komputera pojawia się komunikat "CMOS checksum error press F1 to continue press DEL to setup". Wciśnięcie klawisza DEL spowoduje ', " wejście do BIOS-u komputera ", " usunięcie pliku setup ", " skanowanie zawartości pamięci CMOS ", " przejście do konfiguracji systemu Windows ", " A ")
pyt(" Informacje o błędach działania systemu operacyjnego Linux można uzyskać za pomocą narzędzia ", " netstat ", " syslog ", " watch ", " grub ", " B ")

print()

print("function checkCorrectAnswer(questionNumber) {")
print("  switch (questionNumber) {")
for pop, num in zip(odp_pop, odp_num):
    print("    case "+str(num)+":")
    print("      return '"+pop+"';")
print("    default:")
print("      return '';")
print("  }")
print("}")

