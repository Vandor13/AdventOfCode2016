from tkinter import *
from tkinter.ttk import *
from AoCGui import AoCGui

EXAMPLE_DATA = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn"""


class SignalNoise(AoCGui):
    def __init__(self):
        super().__init__()
        self.data_lines = list(EXAMPLE_DATA.split("\n"))
        self.decoded_message = ""
        self.prepare_gui("Day 7: Internet Protocol Version 7", "Find IP addresses", EXAMPLE_DATA)
        self.no_chars = 0

    def button_pressed(self):
        self.load_text_box_data()
        if self.part.get() == 1:
            self.find_abbas_tls()
        else:
            self.find_abbas_ssl()

    def find_abbas_tls(self):
        tls_ip_addresses = []
        for ip_address in self.data_lines:
            abba_found = False
            in_bracket = False
            for i in range(3, len(ip_address)):
                possible_abba = ip_address[i-3:i+1]
                if "[" in possible_abba:
                    in_bracket = True
                    continue
                elif "]" in possible_abba:
                    in_bracket = False
                    continue
                elif (possible_abba[0] == possible_abba[3]
                      and possible_abba[1] == possible_abba[2]
                      and possible_abba[0] != possible_abba[1]
                ):
                    abba_found = True
                    if in_bracket:
                        break
            if abba_found and not in_bracket:
                tls_ip_addresses.append(ip_address)
        result_text = "Number of TLS IP Addresses: " + str(len(tls_ip_addresses))
        self.set_label(result_text)

    def find_abbas_ssl(self):
        ssl_ip_addresses = []
        for ip_address in self.data_lines:
            abas = []
            babs = []
            aba_and_bab_found = False
            inside_brackets = False
            for i in range(2, len(ip_address)):
                possible_abba = ip_address[i - 2:i + 1]
                if "[" in possible_abba:
                    inside_brackets = True
                    continue
                elif "]" in possible_abba:
                    inside_brackets = False
                    continue
                elif (possible_abba[0] == possible_abba[2]
                      and possible_abba[0] != possible_abba[1]
                ):
                    if not inside_brackets:
                        abas.append(possible_abba)
                    else:
                        babs.append(possible_abba)
            for aba in abas:
                bab = aba[1] + aba[0] + aba[1]
                if bab in babs:
                    aba_and_bab_found = True
                    break
            if aba_and_bab_found:
                ssl_ip_addresses.append(ip_address)
        result_text = "Number of SSL IP Addresses: " + str(len(ssl_ip_addresses))
        self.set_label(result_text)


signal_noise = SignalNoise()
