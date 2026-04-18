# SmileOS Project

This project is still being developed. I aim to create an app that is similar to SmileOS from ULTRAKILL.



### Main Components

- **main.py** - Entry point of the application
- **GUI/** - User interface modules
  - `main_page.py` - Primary interface
  - `side_page.py` - Secondary interface panel
- **Data/** - Data management and processing
  - `customTheme.json` - Theme configuration
  - `ExtraData/` - Data processing and book/testament files
    - `dataProcess.py` - Data processing logic
    - `Books/` - Book data files
    - `Testaments/` - Testament data files
  - `SystemData/` - System configuration modules
    - `guiConfig.py` - GUI configuration
    - `system_info.py` - System information
    - `time_info.py` - Time utilities

### Requirements

This project requires Python 3.8 or higher and runs on **Windows only** (due to WMI dependency).

### Installation

1. **Clone or download the project** to your local machine.

2. **Install required dependencies** by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

3. **Verify installation** - All libraries should install successfully without errors.

### How To Run

Execute the application using:

```bash
python main.py
```

The SmileOS interface will launch in a new window. Use the GUI to navigate between Testaments, Books, and other sections.

### Troubleshooting

- **WMI errors on Windows**: Ensure you're running the terminal as Administrator
- **Module not found errors**: Verify all dependencies are installed with `pip install -r requirements.txt`