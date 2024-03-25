# Django's Ice Cream Shop
 This is a Django-powered inventory tracking application for an ice cream shop. Users can navigate to `/shop` to check out what the store has to offer. Admins can use the `/admin` page to add and remove treats in different flavors. 

 Created by: [github.com/mejia-dev](https://github.com/mejia-dev)

# Features:
* Treats and Flavors have a many-to-many relationship; one treat can have multiple flavors, and one flavor can have multiple treats.
* Django admin system is utilized for ease of administration.
* Shop pages are extensions of a base template for ease of making global changes.

## 1 - Setup/Installation Prerequisite Requirements
This section will cover how to install MySQL Community Server which is **required**. If this application is already installed and running at version 8.0 or above, proceed to the section [Project Setup Requirements](#2---project-setup-requirements) section below.

#### MacOS Instructions:

##### MacOS Step 1: Download the MySQL Community Server Installer
* Start by downloading the MySQL Community Server .dmg file from the MySQL Community Server page:

  For [Catalina and above, AND an M2 chip](https://dev.mysql.com/downloads/file/?id=518602)

  For [Catalina and above, AND an M1 chip](https://dev.mysql.com/downloads/file/?id=508094)

  For [Catalina and above, AND an Intel chip](https://dev.mysql.com/downloads/file/?id=508095)

  For [High Sierra or Mojave](https://dev.mysql.com/downloads/file/?id=484914)


##### MacOS Step 2: Install MySQL Community Server
* Launch the installer. Accept all prompts until reaching the Configuration page. Upon reaching Configuration, select or set the following options (use default if not specified):

  * Use Legacy Password Encryption.
  * Set the password. This password will become necessary later for project setup.
  * Select "Finish".


##### MacOS Step 3: Configure Environment Variables
* Open the terminal to set environment variables using either of the following commands. When finished, close all terminal windows.

  * For bash users:
    ```bash
    echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.bash_profile
    ```

  * For zsh users:
    ```bash
    echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.zshrc
    ```


##### MacOS Step 4: Test Installation (MySQL Community Server)
* From a new terminal window, attempt to login to mysql to confirm it is configured properly.
  Substitute "YOUR_PASSWORD_HERE" for the password that was set during installation.

  ```bash
  mysql -uroot -pYOUR_PASSWORD_HERE
  ```
  There will be an intro message, and the prompt should change to: `mysql> `. This confirms that mysql is installed and everything is working as expected.
  If the terminal instead displays the `mysql: command not found` error, attempt to uninstall any versions of the applications that are previously installed, then follow this installation guide again.


#### Windows 10/11 Instructions:

##### Windows Step 1: Download the MySQL Web Installer
* Download the MySQL Web Installer from the [MySQL Downloads](https://downloads.mysql.com/archives/get/p/25/file/mysql-installer-web-community-8.0.19.0.msi) page. 


##### Windows Step 2: Install the MySQL Web Programs
* Follow along with the installer as described below. If a step is not specifically listed, accept the defaults.

  * Select "Yes" if prompted to update.
  * Accept license terms.
  * Choose "Custom" setup type.
  * In the "Select Products and Features" menu, choose the following:
    * Check the box titled "Enable the Select Features page to customize product features".
    * Under *MySQL Servers > MySQL Server > MySQL Server 8.0*, select "MySQL Server 8.0.19" (or latest available version).
    * Under *Applications > MySQL Workbench > MySQL Workbench 8.0*, select "MySQL Workbench 8.0.19" (or latest available version).
  * Select "Next", then "Execute". Wait for download and installation. This can take some time.
  * Continue through the following Configuration steps:
    * Set "High Availability" to "Standalone".
    * Set "Type and Networking" to "Defaults are OK".
    * Set "Authentication Method" to "Use Legacy Authentication Method".
    * Set the password. This password will become necessary later for project setup.
    * Set "Windows Service" to "Defaults are OK". Ensure that the following options are selected:
      * "Configure MySQL Server as a Windows Service".
      * "Start the MySQL Server at System Startup".
      * "Run Windows Service" should be set to "Standard System Account".
  * Complete the installation as prompted.


##### Windows Step 3: Configure Environment Variables
* The terminal (CLI, PowerShell, and GitBash) now need to be configured to recognize the mysql command. This can be done through changing the environment variables.

  * Press the **Windows** key and **R** key simultaneously to bring up the Run prompt. 
  * In the run prompt, type in `sysdm.cpl`, then press Enter.
  * In the System Properties window that appears, navigate to the "Advanced" tab, then select "Environment Variables...".
    * In the Environment Variables window, under the "System Variables" section, double-click on the "Path" variable to launch the editing window.
      * In the editing window, select the "New" button in the top right, then enter the installation path of the MySQL Server. 
      For most installations, this should be `C:\Program Files\MySQL\MySQL Server 8.0\bin`, but may vary depending on the version installed.
      * When finished, select "OK".
    * Select "OK".
  * Select "Apply", then select "OK".


##### Windows Step 4: Test Installation (MySQL Community Server)
* Finally, from a new PowerShell window, attempt to login to mysql to confirm it is configured properly.
  Substitute "YOUR_PASSWORD_HERE" for the password set during installation.

  ```powershell
  mysql -uroot -pYOUR_PASSWORD_HERE.
  ```

  There will be an intro message, and the prompt should change to: `mysql> `. This confirms that mysql is installed and everything is working as expected.
  If the terminal instead displays a `The term 'mysql' is not recognized as the name of a cmdlet, function, script file, or operable program` error, double-check that the environment variables were set up correctly. If all else fails, attempt to uninstall any versions of the applications that are previously installed, then follow this installation guide again.



## 2 - Project Setup Requirements

#### Step 1: Clone Repo
* Clone this repository by running the following command from in the Git Bash terminal:
  ```bash
   git clone https://github.com/mejia-dev/ice_cream_shop.git
   ```

#### Step 2: Create .env
* This project requires a file titled `.env` residing in the project directory (not the root directory).
  * Navigate to the project directory:
    ```bash
    cd ice_cream_shop/icecreamshop
    ```
  * Create the file:
    ```bash
    touch .env
    ```
  * Using any text editor, modify the file to include the following lines. Replace any of the values with the necessary values for the database environment being used:
    ```json
    DBCONFIG_NAME = "django-icecreamshop"
    DBCONFIG_USER = "YOUR_USERNAME_HERE"
    DBCONFIG_PASSWORD= "YOUR_PASSWORD_HERE"
    DBCONFIG_HOST= "localhost"
    DBCONFIG_PORT= "3306"
    ```



## 3 - Run the Project

* Create a virtual environment for the project. This can be named anything (though `venv` is common) and can be stored anywhere (storing it in the `ice_cream_shop` directory is acceptable, but make sure it is excepted in the gitignore if pushing changes to GitHub). For more information on virtual environments, refer to the [official Python documentation](https://docs.python.org/3/tutorial/venv.html). 
  ```bash
  cd ice_cream_shop
  python -m venv venv
  ```

* Activate the virtual environment in the terminal:

  * Windows:
    ```cmd
    venv\Scripts\activate
    ```
  * Unix / MacOS:
    ```cmd
    source venv/bin/activate
    ```

* Install the requirements from the ice_cream_shop root directory:
  ```bash
  pip install  -r requirements.txt
  ```

* Create the database:
  ```bash
  ./manage.py migrate
  ```

* Create a Django admin account. A prompt will appear for a username, email address, and password.
  ```bash
  manage.py createsuperuser
  ```

* Run the Django development server:
  ```bash
  ./manage.py runserver
  ```

* View the project in a browser by navigating to http://127.0.0.1:8000/shop (for the Shop page) or http://127.0.0.1:8000/admin (for the Admin page).
  ```bash
  dotnet run
  ```


## Known Bugs

* none

If a bug has been discovered, please add it to the [Issues tracker](https://github.com/mejia-dev/ice_cream_shop/issues).


## License

MIT License

Copyright (c) 2023 github.com/mejia-dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
