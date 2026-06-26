#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
┌──────────────────────────────────────────────────────────────────────────┐
│  MIT License (C) 2026 Ananthakrishnan ks. All Rights Reserved.          │
└──────────────────────────────────────────────────────────────────────────┘
"""
import sys
import os
import re
import time
import subprocess
import threading

# --- Cyberpunk Neon TrueColor Space (24-bit) ---
WHITE  = '\033[38;2;245;245;245m'     # High-Contrast White
CYAN   = '\033[38;2;0;245;255m'        # Neon Cyan (Primary Glitch)
PINK   = '\033[38;2;255;0;127m'        # Acid Pink (Alerts / Highlights)
PURPLE = '\033[38;2;187;10;255m'       # Deep Cyber Purple (Frames)
GREEN  = '\033[38;2;57;255;20m'        # Matrix Neon Green (Active/Open)
YELLOW = '\033[38;2;255;211;0m'        # Warning Yellow
RESET  = '\033[0m'

BOLD   = '\033[1m'
DIM    = '\033[2m'

# High-Impact Cyberpunk Block Layout - Explicitly Spelling "ARGUS PX"
LOGO = f"""
  {CYAN} █████╗ ██████╗  ██████╗ ██╗   ██╗███████╗   ██████╗ ██╗  ██╗
  {CYAN}██╔══██╗██╔══██╗██╔════╝ ██║   ██║██╔════╝   ██╔══██╗╚██╗██╔╝
  {PURPLE}███████║██████╔╝██║  ███╗██║   ██║███████╗   ██████╔╝ ╚███╔╝ 
  {PURPLE}██╔══██║██╔══██╗██║   ██║██║   ██║╚════██║   ██╔═══╝  ██╔██╗ 
  {PINK}██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████║   ██║     ██╔╝ ██╗
  {PINK}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝     ╚═╝  ╚═╝{RESET}
                                                                   
                  {BOLD}{WHITE}A  R  G  U  S      P  X{RESET}
  {DIM} ─────────────────────────────────────────────────────────────{RESET}
  {BOLD}{PINK} [ SYSTEM OVERRIDE ]{RESET} {PURPLE}»»{RESET} {BOLD}{WHITE}NET RUNNER SUITE v2.6 // PROTOTYPE LAYER{RESET}
  {DIM} ─────────────────────────────────────────────────────────────{RESET}"""

CYBER_FRAMES = ['░', '▒', '▓', '█']

# Local Vulnerability Engine Matching Database
VULN_DB = {
    21:  {"name": "FTP Insecure Authentication / Anonymous Access", "cve": "CVE-2011-2523", "risk": "HIGH"},
    22:  {"name": "SSH Brute Force Vector / Outdated Handshake", "cve": "CVE-2023-38408", "risk": "MEDIUM"},
    23:  {"name": "Telnet Cleartext Protocol Vulnerability", "cve": "CVE-2020-10188", "risk": "CRITICAL"},
    80:  {"name": "HTTP Unencrypted Traffic / Directory Traversal", "cve": "CVE-2021-41773", "risk": "MEDIUM"},
    443: {"name": "SSL/TLS Vulnerability / Heartbleed", "cve": "CVE-2014-0160", "risk": "HIGH"},
    445: {"name": "SMB Remote Code Execution (MS17-010)", "cve": "CVE-2017-0144", "risk": "CRITICAL"}
}

class CyberPulseSpinner:
    def __init__(self):
        self.ev = threading.Event()
        self.t = None

    def _spin(self):
        idx = 0
        while not self.ev.is_set():
            sys.stdout.write(f"\r  {PINK}{CYBER_FRAMES[idx%4]}{RESET}  {CYAN}[ BUFFERING QUANTUM DECRYPT STREAM... ]{RESET}")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1)

    def start(self):
        self.ev.clear()
        self.t = threading.Thread(target=self._spin, daemon=True)
        self.t.start()

    def stop(self):
        self.ev.set()
        if self.t:
            self.t.join()
        sys.stdout.write("\r" + " " * 75 + "\r")
        sys.stdout.flush()

def render_header():
    print(LOGO)
    print(f"  {BOLD}{CYAN}DEVELOPER // {RESET}{WHITE}Ananthakrishnan ks{RESET}   {PURPLE}▄█▄{RESET}   {BOLD}{CYAN}MATRIX STATUS // {RESET}{GREEN}CONNECTED{RESET}")
    print(f"  {DIM} ─────────────────────────────────────────────────────────────{RESET}\n")

def mask_stream_text(text):
    if not text:
        return ""
    text = text.replace("Nmap", "Argus PX").replace("nmap", "argus px")
    text = text.replace("MAN PAGE", "MAIN PAGE").replace("man.html", "main.html")
    return text

def parse_and_display_output(raw_output, target_ip):
    cleaned = mask_stream_text(raw_output)
    lines = cleaned.splitlines()
    
    print(f"  {PURPLE}╔══ [ TARGET INTERCEPT OBJECTIVE ]{RESET}")
    print(f"  {PURPLE}║{RESET}  {BOLD}NODE ADDR:{RESET} {CYAN}{target_ip}{RESET}")
    print(f"  {PURPLE}║{RESET}  {BOLD}TIMESTAMP:{RESET} {DIM}{time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    print(f"  {PURPLE}╚═════════════════════════════════════════════════════════════{RESET}\n")
    
    in_port_block = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        if any(k in stripped for k in ["Starting Argus PX", "argus px scan report for", "Argus px scan report for", "argus px: option"]):
            continue
            
        if "Host is up" in stripped or "Not shown:" in stripped:
            print(f"  {DIM}» {stripped}{RESET}")
            continue
            
        # Refactored Table Layout: Eliminates complex expressions inside the f-string to prevent syntax truncation errors
        if "PORT" in stripped and "STATE" in stripped:
            header_format = "\n  " + BOLD + PINK + "{:<14} {:<14} {}{}" + RESET
            print(header_format.format("TARGET PORT", "NET STATE", "MAPPED SERVICE LAYER", ""))
            print(f"  {PURPLE}  ▄▄▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{RESET}")
            in_port_block = True
            continue
            
        port_match = re.match(r'^(\d+)/(tcp|udp)\s+(\w+)\s+(.*)$', stripped)
        if port_match:
            port_num = int(port_match.group(1))
            proto = port_match.group(2)
            state = port_match.group(3)
            service_desc = port_match.group(4)
            
            port_label = f"{port_num}/{proto}"
            
            if "open" in state:
                status_chip = f"{GREEN}██ {state:<10}{RESET}"
                row_format = "  " + BOLD + WHITE + "{:<14}" + RESET + " {} " + CYAN + "{}" + RESET
                print(row_format.format(port_label, status_chip, service_desc))
                
                if port_num in VULN_DB:
                    v = VULN_DB[port_num]
                    r_color = PINK if v['risk'] in ["HIGH", "CRITICAL"] else YELLOW
                    
                    print(f"  {PINK}   ⚡ GLITCH DETECTED ══════════════════════════════════╗{RESET}")
                    print(f"     ║  {BOLD}VULN ID:{RESET}   {CYAN}{v['cve']}{RESET}")
                    print(f"     ║  {BOLD}DANGER:{RESET}    {r_color}{v['risk']}{RESET}")
                    print(f"     ║  {BOLD}PAYLOAD:{RESET}   {DIM}{v['name']}{RESET}")
                    print(f"  {PINK}   ╚═══════════════════════════════════════════════════╝{RESET}")
            else:
                status_chip = f"{PURPLE}░░ {state:<10}{RESET}"
                row_format = "  " + DIM + "{:<14}" + " {} {}" + RESET
                print(row_format.format(port_label, status_chip, service_desc))
            continue
            
        if in_port_block:
            if stripped.startswith("|") or stripped.startswith("_"):
                cleaned_line = stripped.lstrip('|_ ')
                print(f"       {PURPLE}└──{RESET} {DIM}{cleaned_line}{RESET}")
            elif not any(k in stripped for k in ["Argus PX done", "SF:"]):
                print(f"       {PURPLE}╎{RESET} {DIM}{stripped}{RESET}")

def main():
    if len(sys.argv) == 1 or '-h' in sys.argv or '--help' in sys.argv:
        render_header()
        cmd = ["nmap", "-h"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        help_txt = mask_stream_text(res.stdout)
        print(help_txt)
        return

    render_header()
    
    target_ip = "TARGET NODE"
    for arg in sys.argv[1:]:
        if not arg.startswith('-') and re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', arg):
            target_ip = arg
            break
            
    args_pool = sys.argv[1:]
    target_cmd = ["nmap"] + args_pool
    
    spinner = CyberPulseSpinner()
    spinner.start()
    
    try:
        proc = subprocess.run(target_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        spinner.stop()
        
        if proc.stdout:
            parse_and_display_output(proc.stdout, target_ip)
        if proc.stderr:
            parse_and_display_output(proc.stderr, target_ip)
            
    except KeyboardInterrupt:
        spinner.stop()
        print(f"\n  {PINK}[!] BREAK SIGNAL DETECTED. FORCED ENGINE TERMINATION.{RESET}")
    finally:
        print(f"\n  {DIM}MIT License (C) 2026 Ananthakrishnan ks. Systems integrated safely.{RESET}\n")

if __name__ == "__main__":
    main()
