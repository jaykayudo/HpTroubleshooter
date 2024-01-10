import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox


# Define classes and functions
class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

class KnowledgeBase:
    def __init__(self):
        self.rules = []
        self.facts = []

    def add_rule(self, rule):
        self.rules.append(rule)


def matches(antecedent, facts):
    pass


def infer(facts):
    # Check if any rules have antecedents matching the known facts
    for rule in knowledge_base.rules:
        if matches(rule.antecedent, facts):
            # Add consequent to facts if antecedent matches
            facts.append(rule.consequent)


# Create knowledge base
knowledge_base = KnowledgeBase()

knowledge_base = [
    dict(issue='Laptop not turning on', symptoms=['No power indicator'],
         solution='Follow these steps:\n\nStep 1: Verify Power Source\nEnsure that the laptop is connected to a working power source, either through the AC adapter or a charged battery.\n\nStep 2: Check Power Indicator\nLook for the power indicator light on the laptop.\nIf it is not illuminated, the laptop might not be receiving power.\n\nStep 3: Test the AC Adapter\nCheck the AC adapter for any physical damage or frayed cables.\nIf possible, test the AC adapter with another HP laptop to confirm if it is working.\n\nStep 4: Inspect Battery\nIf using a battery, remove it and reinsert it properly.\nTest the laptop with just the AC adapter (remove the battery) to check if it powers on.\n\nStep 5: Try Another Outlet\nPlug the AC adapter into a different power outlet to eliminate the possibility of a faulty outlet.'),
    dict(issue='Laptop still not turning on', symptoms=['No response when pressing power button'],
         solution='Follow these steps:\n\nStep 1: Perform a Hard Reset\nDisconnect the AC adapter and remove the laptop battery.\nPress and hold the power button for about 15 seconds.\nReconnect the battery and AC adapter.\n\nStep 2: Test Without Battery\nRemove the laptop battery and connect the AC adapter.\nAttempt to turn on the laptop without the battery.\n\nStep 3: Reseat RAM and Hard Drive\nTurn off the laptop and disconnect the AC adapter.\nCarefully open the laptop\'s access panel to access the RAM and hard drive.\nGently remove and reseat the RAM modules and hard drive to ensure they are properly connected\n\nStep 4: Check for LED Lights\nWhen you press the power button, observe if any LED lights or indicators blink briefly.\nIf they do, it indicates that power is reaching the laptop.\n\nStep 5: Hardware Diagnostic Test (if available)\nSome HP laptops come with built-in hardware diagnostic tests.\nFollow the manufacturer\'s instructions to run these tests and identify potential hardware issues.'),
    dict(issue='Overheating', symptoms=['Laptop getting excessively hot'],
         solution='Follow these steps:\n\nStep 1: Check Ventilation\nEnsure that the laptop is placed on a flat, hard surface to allow proper airflow.\nCheck that the ventilation grilles and fan vents are not obstructed by dust or debris.\n\nStep 2: Clean the Vents and Fans\nTurn off the laptop and unplug it.\nUse compressed air to gently blow out dust and debris from the vents and fan openings.\nBe careful not to damage the fan blades or push debris further into the laptop.\n\nStep 3: Adjust Power Settings\nNavigate to the Control Panel or Settings and access the Power Options.\nChoose a power plan that balances performance with energy efficiency.\nYou can also manually adjust the settings to reduce the laptop\'s processing power when on battery to prevent overheating.\n\nStep 4: Update Drivers and BIOS\nVisit the official HP website and download the latest drivers and BIOS updates for your laptop model.\nInstall the updates to ensure optimal performance and temperature management.\n\nStep 5: Use a Cooling Pad\nConsider using a laptop cooling pad with built-in fans to improve airflow and dissipate heat.'),
    dict(issue='Still Overheating', symptoms=['Fan making loud noises'],
         solution='Follow these steps:\n\nStep 1: Check for Obstructions\nTurn off the laptop and unplug it.\nExamine the fan vent openings for any foreign objects that might be causing the noise.\n\nStep 2: Clean the Fan\nIf there is visible dust or debris on the fan blades, carefully open the laptop\'s access panel.\nUse compressed air to gently clean the fan blades, ensuring not to damage them.\n\nStep 3: Update BIOS and Drivers\nAs with the overheating issue, ensure your laptop\'s BIOS and drivers are up to date.\n\nStep 4: Adjust Fan Settings\nSome laptops allow you to adjust fan settings through the BIOS or specific software.\nChoose a fan profile that balances noise reduction with cooling efficiency.\n\nStep 5: Monitor Background Processes\nExcessive background processes or running software can cause the fan to work harder.\nClose unnecessary programs to see if the noise diminishes.\n\nStep 6: Professional Inspection\nIf the loud noise persists, it might indicate a mechanical issue with the fan.\n\nAlways remember to exercise caution while working with hardware components, and if you are unsure or uncomfortable with performing these steps, seek professional help.'),
    dict(issue='Battery not charging', symptoms=['Battery percentage not increasing'],
         solution='Issue 1: Battery Percentage Not Increasing\n\nStep 1: Verify Charging Source\nEnsure that the laptop is connected to a working power source through the AC adapter.\nCheck if the charging cable is securely connected to both the laptop and the power outlet.\n\nStep 2: Restart the Laptop\nSometimes, a simple restart can help reset the battery management system.\nSave your work, shut down the laptop, and then power it on again.\n\nStep 3: Check Battery Health\nOpen the laptop\'s battery health utility (if available) to check for any issues or recommendations.\nWindows users can also use the built-in Battery Report feature to assess the battery\'s health.\n\nStep 4: Perform a Battery Calibration (Optional)\nAllow the battery to discharge until the laptop shuts down due to low battery.\nPlug in the AC adapter and charge the laptop to 100% without interruption.\nThis process can recalibrate the battery\'s reporting accuracy.'),
    dict(issue='Battery still not charging', symptoms=['No charging indicator'],
         solution='Follow these steps:\n\nStep 1: Check Charging LED\nLook for the charging LED indicator on the laptop.\nIf the LED is not illuminated, the laptop might not be receiving power.\n\nStep 2: Inspect AC Adapter\nExamine the AC adapter for any damage to the cables or connectors.\nTest the AC adapter on another device (if possible) to confirm its functionality.\n\nStep 3: Verify Charging Port\nEnsure that the charging port on the laptop is not obstructed and that the pins are not bent or damaged.\n\nStep 4: Test with Another Outlet\nPlug the AC adapter into a different power outlet to rule out issues with the power source.\n\nStep 5: Update BIOS and Drivers\nVisit the official HP website and download the latest BIOS and driver updates for your laptop.\nSometimes, firmware updates can resolve charging-related issues.\n\nStep 6: Perform a Hard Reset\nDisconnect the AC adapter and remove the laptop battery.\nPress and hold the power button for about 15 seconds.\nReconnect the battery and AC adapter.'),
    dict(issue='Wi-Fi connectivity issues', symptoms=['Unable to connect to Wi-Fi network'],
         solution='Follow these steps:\n\nStep 1: Check Wi-Fi Switch/Key\nEnsure the physical Wi-Fi switch (if your laptop has one) is turned on.\nCheck if you\'ve accidentally disabled Wi-Fi using the function keys (like F2) on your laptop.\n\nStep 2: Restart Router\nPerform the router power cycle as explained in the previous section.\n\nStep 3: Forget and Reconnect to Network\nGo to the Wi-Fi settings on your laptop.\nForget the problematic network and then reconnect by entering the correct password.\n\nStep 4: Update Wi-Fi Driver\nUpdate the Wi-Fi driver as explained in the previous section.\n\nStep 5: Troubleshoot Network Adapter\nOpen the Windows Network Troubleshooter from the Control Panel or Settings.\nFollow the prompts to diagnose and fix network connection issues.\n\nStep 6: Reset Network Settings\nIn the Control Panel or Settings, navigate to Network & Internet > Network Reset.\nResetting network settings can often resolve persistent connectivity problems.'),
    dict(issue='Wi-Fi connection issues', symptoms=['Frequent disconnections'],
         solution='Follow these steps:\n\nStep 1: Check Wi-Fi Signal Strength\nEnsure you\'re within the range of your Wi-Fi router.\nCheck the signal strength indicator on your laptop to confirm a strong connection.\n\nStep 2: Restart Router\nPower cycle your Wi-Fi router by unplugging it, waiting for about 10 seconds, and plugging it back in.\nWait for the router to fully restart and then check the connection stability.\n\nStep 3: Update Wi-Fi Driver\nVisit the official HP website and download the latest Wi-Fi driver for your laptop.\nInstall the driver update to ensure compatibility and stability.\n\nStep 4: Disable Power Saving for Wi-Fi\nGo to the Control Panel or Settings and navigate to Power Options.\nAdjust the power plan settings to prevent the Wi-Fi adapter from going to sleep.\n\nStep 5: Check for Interference\nNearby electronic devices or physical obstacles can interfere with Wi-Fi signals.\nEnsure your laptop is away from devices like microwaves, cordless phones, and thick walls.\n\nStep 6: Change Wi-Fi Channel\nAccess your router\'s settings and try changing the Wi-Fi channel to a less crowded one.\nThis can improve connection stability by reducing interference.'),
    dict(issue='Blue screen of death (BSOD)', symptoms=['Frequent system crashes with blue screen'],
         solution='Follow these steps:\n\nStep 1: Update Windows and Drivers\nEnsure that your Windows operating system and all drivers are up to date.\nVisit the Windows Update settings and HP\'s official website to download driver updates.\n\nStep 2: Check for Overheating\nOverheating can cause system instability. Make sure your laptop is placed on a flat surface and its vents are clear of dust.\nUse compressed air to clean out any dust from the cooling system.\n\nStep 3: Run System File Checker (SFC)\nOpen Command Prompt as an administrator.\nType sfc /scan now and press Enter to check for and repair any corrupted system files.\n\nStep 4: Run Windows Memory Diagnostic\nSearch for "Windows Memory Diagnostic" in the Windows search bar and run the tool to check for memory issues.\n\nStep 5: Check for Malware\nRun a full system scan using a reputable antivirus or Windows Defender to rule out malware causing crashes.\n\nStep 6: Uninstall Recently Installed Software\nIf the crashes started after installing new software, uninstall it and check if the issue persists.\n\nStep 7: Check for Hardware Issues\nIf the crashes persist, there could be hardware problems. Run built-in hardware diagnostic tests if available.'),
    dict(issue='Blue screen of death (BSOD)', symptoms=['Error codes displayed during crashes'],
         solution='Follow these steps:\n\nStep 1: Document the Error Code\nWhen your laptop crashes, take note of the specific error code displayed on the blue screen.\n\nStep 2: Research the Error Code\nSearch for the error code online to get more information about its potential causes and solutions.\n\nStep 3: Check for Specific Drivers or Software\nSome error codes are associated with specific drivers or software. Check if the error is related to a specific component.\n\nStep 4: Rollback or Update Drivers\nIf a specific driver is causing the crash, try rolling it back to a previous version or updating to the latest version.\n\nStep 5: Check for Recent Hardware Changes\nIf you recently added or upgraded hardware components, such as RAM or a hard drive, ensure they are properly installed and compatible.\n\nStep 6: Check Event Viewer\nOpen Event Viewer in Windows and navigate to "Windows Logs" > "System" to view detailed error logs that might provide insights into the crashes.'),
    dict(issue='No sound', symptoms=['No sound from speakers'],
         solution='Follow these steps:\n\nStep 1: Check Volume and Mute\nMake sure the volume is not muted and turned up on your laptop.\nAdjust the volume using the physical volume buttons on your laptop.\n\nStep 2: Check Audio Output\nRight-click the volume icon in the taskbar and select "Open Sound settings."\nEnsure that the correct output device (speakers) is selected.\n\nStep 3: Test Different Audio Sources\nPlay audio from different sources (e.g., YouTube, local files) to rule out issues with specific applications.\n\nStep 4: Check Audio Jacks\nIf you\'re using headphones, ensure they are properly plugged into the correct audio jack.\n\nStep 5: Update Audio Drivers\nVisit the official HP website and download the latest audio driver for your laptop model.\nInstall the driver update to ensure proper audio functionality.\n\nStep 6: Run Windows Troubleshooter\nRight-click the volume icon in the taskbar and select "Troubleshoot sound problems."\nFollow the prompts to diagnose and potentially fix sound-related issues.'),
    dict(issue='Other audio issues', symptoms=['Audio playback distorted'],
         solution='Follow these steps:\n\nStep 1: Check Volume Levels\nEnsure the volume is not set too high, as excessive volume can cause distortion.\n\nStep 2: Test Different Audio Sources\nPlay audio from different sources to determine if the distortion is specific to certain applications or files.\n\nStep 3: Update Audio Drivers\nAs mentioned earlier, visit the official HP website to download and install the latest audio driver update.\n\nStep 4: Adjust Sound Settings\nRight-click the volume icon in the taskbar and select "Open Sound settings."\nAdjust audio enhancements and equalizer settings to see if they contribute to distortion.\nStep 5: Test Different Output Devices\nTry connecting external speakers or headphones to see if the distortion persists across different output devices.\n\nStep 6: Check for Software Conflicts\nThird-party audio software or applications can sometimes cause distortion.\nTemporarily disable or uninstall any recently installed audio-related software.\n\nStep 7: Perform a Sound Troubleshooting\nOpen Control Panel and search for "Troubleshooting."\nSelect "Troubleshoot audio playback" and follow the prompts to diagnose and fix audio issues.'),
    dict(issue='Hard drive failure or data loss', symptoms=['Clicking or grinding noises from Hard drive'],
         solution='Follow these steps:\n\nStep 1: Backup Important Data\nBefore proceeding, ensure you have a backup of important files, as clicking or grinding noises can indicate a failing hard drive.\n\nStep 2: Confirm the Source of Noise\nGently listen near the laptop\'s hard drive location to confirm if the noise is indeed coming from the hard drive.\n\nStep 3: Diagnose Hard Drive Health\nOpen Command Prompt as an administrator.\nType wmic diskdrive get status and press Enter to check the hard drive\'s health status.'),
    dict(issue='Hard drive failure or data loss', symptoms=['Inability to access files'],
         solution='Follow these steps:\n\nStep 1: Check File Locations\nMake sure you\'re trying to access files from the correct folders or directories.\nStep 2: Run Check Disk (CHKDSK)\nOpen Command Prompt as an administrator.\nType chkdsk /f /r and press Enter to run a disk check that can repair file system errors.\n\nStep 3: Test File Access on Another Device\nTransfer the problematic files to another device (USB drive or another computer) and attempt to access them there.\n\nStep 4: Use Data Recovery Software\nIf files are inaccessible due to corruption, use reputable data recovery software to recover them.\n\nStep 5: Restore from Backup\nIf you have a backup of the files, restore them to their original location.\n\nStep 6: Scan for Malware\nMalware can sometimes prevent access to files. Run a thorough malware scan using a reputable antivirus or Windows Defender.'),
    dict(issue='Software crashes', symptoms=['Frequent application crashes'],
         solution='Follow these steps:\n\nStep 1: Update Applications\nEnsure that the applications you\'re using are up to date.\nVisit the respective app stores or official websites to download any available updates.\n\nStep 2: Check System Requirements\nConfirm that your laptop meets the minimum system requirements for the applications you\'re using.\nSometimes, inadequate hardware can lead to crashes.\n\nStep 3: Disable Add-ons or Plugins\nIf the crashes are happening in web browsers or applications with plugins, try disabling them to see if they\'re causing the issues.\n\nStep 4: Run Applications in Compatibility Mode\nRight-click the application\'s shortcut or executable file.\nSelect "Properties" and navigate to the "Compatibility" tab. Enable compatibility mode for a previous Windows version.\n\nStep 5: Check for Conflicting Software\nSome applications might conflict with each other. Temporarily uninstall or disable recently installed software to identify the cause.\n\nStep 6: Update Graphics Drivers\nVisit the official HP website to download and install the latest graphics drivers for your laptop model.\n\nStep 7: Run Windows Updates\nMake sure your Windows operating system is up to date. Install any available updates.'),
    dict(issue='Unresponsive Software', symptoms=['System becomes unresponsive'],
         solution='Follow these steps:\n\nStep 1: Close Unnecessary Programs\nIf the system becomes sluggish or unresponsive, close any unnecessary programs running in the background.\n\nStep 2: Check Task Manager\nPress Ctrl + Shift + Esc to open Task Manager.\nIdentify any processes consuming excessive CPU or memory resources.\n\nStep 3: Update or Rollback Drivers\nOutdated or incompatible drivers can cause system instability.\nUpdate all drivers or consider rolling back to a previous version if an update caused the issue\n\n.Step 4: Perform Disk Cleanup\nOpen the Windows search bar and type "Disk Cleanup."\nRun the tool to clean up temporary files and free up disk space.\n\nStep 5: Run System File Checker (SFC)\nOpen Command Prompt as an administrator.\nType sfc /scannow and press Enter to check and repair corrupted system files.\n\nStep 6: Check for Malware\nRun a thorough malware scan using a reputable antivirus or Windows Defender.\n\nStep 7: Disable Startup Programs\nOpen Task Manager and navigate to the "Startup" tab.\nDisable unnecessary startup programs that might be slowing down the system.\n\nStep 8: Check for Hardware Issues\nHardware problems can lead to system unresponsiveness. Run built-in hardware diagnostic tests if available.'),
    dict(issue='Virus or malware infections', symptoms=['Slow performance'],
         solution='Follow these steps:\n\nStep 1: Check Resource Usage\nOpen Task Manager by pressing Ctrl + Shift + Esc.\nCheck CPU, memory, and disk usage to identify resource-hungry processes.\n\nStep 2: Close Unnecessary Programs\nClose programs you\'re not actively using to free up system resources.\n\nStep 3: Run Disk Cleanup\nUse the built-in Disk Cleanup tool to remove temporary files and free up disk space.\n\nStep 4: Disable Startup Programs\nOpen Task Manager and navigate to the "Startup" tab.\nDisable unnecessary startup programs to improve boot time and performance.\n\nStep 5: Update Drivers\nVisit the official HP website and download the latest drivers for your laptop model.\nUpdate drivers, especially for graphics and chipset components.\n\nStep 6: Run System File Checker (SFC)\nOpen Command Prompt as an administrator.\nType sfc /scannow and press Enter to check and repair corrupted system files.\n\nStep 7: Scan for Malware\nRun a thorough malware scan using a reputable antivirus or Windows Defender.\n\nStep 8: Disable Visual Effects\nOpen the Control Panel and search for "Performance."\nSelect "Adjust the appearance and performance of Windows."\nChoose the "Adjust for best performance" option or customize visual effects.'),
    dict(issue='Virus or malware infections', symptoms=['Unexpected pop-ups or system behavior'],
         solution='Follow these steps:\n\nStep 1: Update Security Software\nEnsure your antivirus and anti-malware software are up to date.\nPerform a full system scan to detect and remove any threats.\n\nStep 2: Uninstall Suspicious Programs\nOpen the Control Panel and navigate to "Uninstall a program."\nRemove any unfamiliar or suspicious programs.\n\nStep 3: Clear Browser Cache and Cookies\nIn your web browser\'s settings, clear browsing history, cache, and cookies.\n\nStep 4: Reset Browser Settings\nIf pop-ups are browser-related, reset your browser settings to default.\n\nStep 5: Check Browser Extensions\nDisable or remove browser extensions that might be causing pop-ups.\n\nStep 6: Run Adware/Malware Scans\nUse reputable adware/malware removal tools to scan for potentially unwanted programs.\n\nStep 7: Review Recent Software Installs\nIf the unexpected behavior started after installing new software, uninstall it.\n\nStep 8: Disable Notification Permissions\nReview and disable notification permissions for websites that may show pop-ups.'),
    # Add more issues and solutions as needed
                ]


def analyze_symptoms(symptoms):
    for issue in knowledge_base:
        if set(symptoms).issubset(set(issue['symptoms'])):
            return issue['solution']
    return 'No matching issue found.'


def solve_problem():
    symptoms = entry.get().split(', ')
    solution = analyze_symptoms(symptoms)
    result_label.config(text=solution)


def possible_issues():
    symptoms_list = list(map(lambda x: x['symptoms'], knowledge_base))
    main_list = []
    for x in symptoms_list:
        for y in x:
            main_list.append(y)
    string = "\n".join(main_list)
    msgbox.showinfo("Possible Issues", string)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('HP Laptop Troubleshooting Expert System')
    root.geometry("720x600")
    root.resizable(False, False)

    label = ttk.Label(root, text='Enter the symptoms you are experiencing (comma-separated):')
    label.pack()

    entry = ttk.Entry(root)
    entry.pack()

    button = ttk.Button(root, text='Submit', command=solve_problem)
    button.pack()

    button = ttk.Button(root, text='View Possible Issues', command=possible_issues)
    button.pack()
    result_label = ttk.Label(root, text='', wraplength=500)
    result_label.pack()

    root.mainloop()

# Example usage
user_symptoms = ['No power indicator', 'No response when pressing power button']
solution = analyze_symptoms(user_symptoms)
print(solution)

# Combine dataframes
# df = pd.concat([source1, source2])

# # Clean data
# df = df.dropna()
# df = df.drop_duplicates()
# df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# # Extract relevant columns
# cols = ["column1", "column2", "column3"]
# df = df[cols]

# # Save cleaned data
# df.to_csv("cleaned_data.csv", index=False)

# Infer new facts
# infer(facts)

# # Check if issue has been identified
# if "issue1" in facts:
#     print("Potential issue is issue1")

#     from setuptools import setup

APP = ['your_script.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'iconfile': 'icon.icns',  # Optional: Add an icon file
}

# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     setup_requires=['py2app'],
# )
