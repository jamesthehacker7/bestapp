import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

# Define the main window for the app
class MainScreen(toga.App):
    pushup_count = 0
    pullup_count = 0

    def increase_pushup_count(self, widget):
        self.pushup_count += 1
        self.pushup_count_label.text = str(self.pushup_count)

    def increase_pullup_count(self, widget):
        self.pullup_count += 1
        self.pullup_count_label.text = str(self.pullup_count)

    def login(self, widget):
        if self.username_input.value == 'admin' and self.password_input.value == 'admin':
            self.login_button.label = self.username_input.value
            self.username_input.value = ''
            self.password_input.value = ''
        else:
            self.username_input.value = ''
            self.password_input.value = ''
            self.login_error_label.text = 'Invalid username or password'

    def signup(self, widget):
        self.signup_window.show()

    def register(self, widget):
        self.signup_window.hide()
        self.username_input.value = ''
        self.password_input.value = ''
        self.realname_input.value = ''
        # Do something with the user's registration info, like storing it in a database

    def startup(self):
        # Create the main window
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20))
        pushup_box = toga.Box(style=Pack(direction=ROW, padding=10))
        pullup_box = toga.Box(style=Pack(direction=ROW, padding=10))
        login_box = toga.Box(style=Pack(direction=ROW, padding=10))
        signup_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Create the widgets for the pushup count
        pushup_count_box = toga.Box(style=Pack(direction=ROW, padding=10))
        self.pushup_count_label = toga.Label('0', style=Pack(font_size=50))
        pushup_count_box.add(self.pushup_count_label)
        pushup_button = toga.Button('Pushups', on_press=self.increase_pushup_count)
        pushup_count_box.add(pushup_button)
        pushup_box.add(pushup_count_box)

        # Create the widgets for the pullup count
        pullup_count_box = toga.Box(style=Pack(direction=ROW, padding=10))
        self.pullup_count_label = toga.Label('0', style=Pack(font_size=50))
        pullup_count_box.add(self.pullup_count_label)
        pullup_button = toga.Button('Pullups', on_press=self.increase_pullup_count)
        pullup_count_box.add(pullup_button)
        pullup_box.add(pullup_count_box)

        # Create the widgets for the login button
        self.login_button = toga.Button('Login', on_press=self.login, style=Pack(background_color='#FFA500'))
        login_box.add(self.login_button)

        # Create the widgets for the signup button
        signup_button = toga.Button('Sign Up', on_press=self.signup, style=Pack(background_color='#FFA500'))
        login_box.add(signup_button)

        # Create the widgets for the login page
        login_box2 = toga.Box(style=Pack(direction=COLUMN, padding=20))
        login_box2.add(toga.Label('Username:'))
        self.username_input = toga.TextInput()
        login_box2.add(self.username_input)
        login_box2.add(toga.Label('Password:'))

//=================================================================================================//

        self.password_input = toga.PasswordInput()
        login_box2.add(self.password_input)
        login_box2.add(toga.Button('Login', on_press=self.login))
        self.login_error_label = toga.Label('', style=Pack(color='red'))
        login_box2.add(self.login_error_label)

        # Create the widgets for the sign up page
        signup_box.add(toga.Label('Real Name:'))
        self.realname_input = toga.TextInput()
        signup_box.add(self.realname_input)
        signup_box.add(toga.Label('Username:'))
        self.signup_username_input = toga.TextInput()
        signup_box.add(self.signup_username_input)
        signup_box.add(toga.Label('Password:'))
        self.signup_password_input = toga.PasswordInput()
        signup_box.add(self.signup_password_input)
        signup_box.add(toga.Button('Register', on_press=self.register))

        # Create the main box
        main_box.add(pushup_box)
        main_box.add(pullup_box)
        main_box.add(login_box)

        # Create the windows
        self.main_window = toga.MainWindow(title=self.name, size=(400, 400), style=Pack(background_color='#FFA500'))
        self.signup_window = toga.Window(title='Sign Up', size=(300, 300), style=Pack(background_color='#FFA500'))
        self.signup_window.content = signup_box
        self.login_window = toga.Window(title='Login', size=(300, 200), style=Pack(background_color='#FFA500'))
        self.login_window.content = login_box2

        # Show the main window
        self.main_window.content = main_box
        self.main_window.show()

//=====================================================//

class MainScreen(toga.App):
    def startup(self):
        # Define the functionality for the count buttons
        def count_pushup(widget):
            count = int(pushup_number.text)
            count += 1
            pushup_number.text = str(count)

        def count_pullup(widget):
            count = int(pullup_number.text)
            count += 1
            pullup_number.text = str(count)

        # Define the functionality for the login and sign up buttons
        def login(widget):
            if self.username_input.value == 'admin' and self.password_input.value == 'admin':
                self.login_error_label.text = ''
                self.login_window.hide()
                self.main_window.right_toolbar = toga.Label(f'Logged in as {self.username_input.value}')
            else:
                self.login_error_label.text = 'Invalid username or password'

        def register(widget):
            username = self.signup_username_input.value
            password = self.signup_password_input.value
            realname = self.realname_input.value

            # Check if the username is already taken
            if username in self.users:
                toga.window.info_dialog('Error', 'Username already taken')
                return

            # Add the new user
            self.users[username] = {
                'password': password,
                'realname': realname,
            }

            # Switch to the main window
            self.signup_window.hide()
            self.main_window.right_toolbar = toga.Label(f'Logged in as {username}')

        # Create the boxes and widgets
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        pushup_box = toga.Box(style=Pack(direction=ROW, padding=10))
        pushup_number = toga.Label('0', style=Pack(font_size=48))
        pushup_button = toga.Button('Pushups', on_press=count_pushup)
        pushup_box.add(pushup_number)
        pushup_box.add(pushup_button)

        pullup_box = toga.Box(style=Pack(direction=ROW, padding=10))
        pullup_number = toga.Label('0', style=Pack(font_size=48))
        pullup_button = toga.Button('Pullups', on_press=count_pullup)
        pullup_box.add(pullup_number)
        pullup_box.add(pullup_button)

        login_box = toga.Box(style=Pack(direction=ROW, padding=10, alignment=CENTER_RIGHT))
        login_box.add(toga.Button('Login', on_press=lambda widget: self.login_window.show()))
        login_box.add(toga.Button('Sign up', on_press=lambda widget: self.signup_window.show()))

        login_box2 = toga.Box(style=Pack(direction=COLUMN, padding=10))
        login_box2.add(toga.Label('Username:'))
        self.username_input = toga.TextInput()
        login_box2.add(self.username_input)
        login_box2.add(toga.Label('Password:'))
        self.password_input = toga.PasswordInput()
        login_box2.add(self.password_input)
        login_box2.add(toga.Button('Login', on_press=login))
        self.login_error_label = toga.Label('', style=Pack(color='red'))
        login_box2.add(self.login_error_label)

        # Create the widgets for the sign up page
        signup_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        signup_box.add(toga.Label('Real Name:'))
        self.realname_input = toga.TextInput()
        signup_box.add(self.realname_input)


//============================================================//

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER_RIGHT


class MainScreen(toga.App):
    def startup(self):
        # Define the users dictionary
        self.users = {
            'admin': {
                'password': 'admin',
                'realname': 'Administrator',
            }
        }

        # Define the functionality for the count buttons
        def count_pushup(widget):
            count = int(pushup_number.text)
            count += 1
            pushup_number.text = str(count)

        def count_pullup(widget):
            count = int(pullup_number.text)
            count += 1
            pullup_number.text = str(count)

        # Define the functionality for the login and sign up buttons
        def login(widget):
            if self.username_input.value == 'admin' and self.password_input.value == 'admin':
                self.login_error_label.text = ''
                self.login_window.hide()
                self.main_window.right_toolbar = toga.Label(f'Logged in as {self.username_input.value}')
            else:
                self.login_error_label.text = 'Invalid username or password'

        def register(widget):
            username = self.signup_username_input.value
            password = self.signup_password_input.value
            realname = self.realname_input.value

            # Check if the username is already taken
            if username in self.users:
                toga.window.info_dialog('Error', 'Username already taken')
                return

            # Add the new user
            self.users[username] = {
                'password': password,
                'realname': realname,
            }

            # Switch to the main window
            self.signup_window.hide()
            self.main_window.right_toolbar = toga.Label(f'Logged in as {username}')

        # Create the boxes and widgets
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        pushup_box = toga.Box(style=Pack(direction=ROW, padding=10))
        pushup_number = toga.Label('0', style=Pack(font_size=48))
        pushup_button = toga.Button('Pushups', on_press=count_pushup)
        pushup_box.add(pushup_number)
        pushup_box.add(pushup_button)

        pullup_box = toga.Box(style=Pack(direction=ROW, padding=10))
        pullup_number = toga.Label('0', style=Pack(font_size=48))
        pullup_button = toga.Button('Pullups', on_press=count_pullup)
        pullup_box.add(pullup_number)
        pullup_box.add(pullup_button)

        login_box = toga.Box(style=Pack(direction=ROW, padding=10, alignment=CENTER_RIGHT))
        login_box.add(toga.Button('Login', on_press=lambda widget: self.login_window.show()))
        login_box.add(toga.Button('Sign up', on_press=lambda widget: self.signup_window.show()))

        login_box2 = toga.Box(style=Pack(direction=COLUMN, padding=10))
        login_box2.add(toga.Label('Username:'))
        self.username_input = toga.TextInput()
        login_box2.add(self.username_input)
        login_box2.add(toga.Label('Password:'))
        self.password_input = toga.PasswordInput()
        login_box2.add(self.password_input)
        login_box2.add(toga.Button('Login', on_press=login))
        self.login_error_label = toga.Label('', style=Pack(color='red'))
        login_box2.add(self

        //================================================================================================================================

        import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER_RIGHT


class MainScreen(toga.App):
    def startup(self):
        # Define the users dictionary
        self.users = {
            'admin': {
                'password': 'admin',
                'realname': 'Administrator',
            }
        }

        # Define the functionality for the count buttons
        def count_pushup(widget):
            count = int(pushup_number.text)
            count += 1
            pushup_number.text = str(count)

        def count_pullup(widget):
            count = int(pullup_number.text)
            count += 1
            pullup_number.text = str(count)

        # Define the functionality for the login and sign up buttons
        def login(widget):
            if self.username_input.value == 'admin' and self.password_input.value == 'admin':
                self.login_error_label.text = ''
                self.login_window.hide()
                self.main_window.right_toolbar = toga.Label(f'Logged in as {self.username_input.value}')
            else:
                self.login_error_label.text = 'Invalid username or password'

        def register(widget):
            username = self.signup_username_input.value
            password = self.signup_password_input.value
            realname = self.realname_input.value

            # Check if the username is already taken
            if username in self.users:
                toga.window.info_dialog('Error', 'Username already taken')
                return

            # Add the new user
            self.users[username] = {
                'password': password,
                'realname': realname,
            }

            # Switch to the main window
            self.signup_window.hide()
            self.main_window.right_toolbar = toga.Label(f'Logged in as {username}')

        # Create the boxes and widgets
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        pushup_box = toga.Box(style=Pack(direction=ROW, padding=10))
        pushup_number = toga.Label('0', style=Pack(font_size=48))
        pushup_button = toga.Button('Pushups', on_press=count_pushup)
        pushup_box.add(pushup_number)
        pushup_box.add(pushup_button)

        pullup_box = toga.Box(style=Pack(direction=ROW, padding=10))
        pullup_number = toga.Label('0', style=Pack(font_size=48))
        pullup_button = toga.Button('Pullups', on_press=count_pullup)
        pullup_box.add(pullup_number)
        pullup_box.add(pullup_button)

        login_box = toga.Box(style=Pack(direction=ROW, padding=10, alignment=CENTER_RIGHT))
        login_box.add(toga.Button('Login', on_press=lambda widget: self.login_window.show()))
        login_box.add(toga.Button('Sign up', on_press=lambda widget: self.signup_window.show()))

        login_box2 = toga.Box(style=Pack(direction=COLUMN, padding=10))
        login_box2.add(toga.Label('Username:'))
        self.username_input = toga.TextInput()
        login_box2.add(self.username_input)
        login_box2.add(toga.Label('Password:'))
        self.password_input = toga.PasswordInput()
        login_box2.add(self.password_input)
        login_box2.add(toga.Button('Login', on_press=login))
        self.login_error_label = toga.Label('', style=Pack(color='red'))
        login_box2.add(self.login_error_label)

        signup_box = toga.Box(style=Pack(direction=COLUMN, padding=10

//============================================================================

class PushupsWindow(toga.Window):
    def __init__(self):
        super().__init__(title='Pushups', size=(150, 150))
        
        self.count = 0

        # create label for count
        self.count_label = toga.Label(
            '0',
            style=Pack(font_size=72, padding=20)
        )

        # create button for incrementing count
        self.increment_button = toga.Button(
            'Click to Add',
            on_press=self.increment_count,
            style=Pack(flex=1, padding=20)
        )

        # create box container for label and button
        box = toga.Box(
            children=[self.count_label, self.increment_button],
            style=Pack(direction='column', alignment='center', padding=20)
        )

        # add the box container to the main window
        self.content = box

    def increment_count(self, widget):
        self.count += 1
        self.count_label.text = str(self.count)
