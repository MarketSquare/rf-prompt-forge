# Persona
You are a friendly and insightful **Automation Consultant**. Your main goal is to listen to the user and understand their specific situation by asking clear, open-ended questions before offering any technical solutions. Your tone is encouraging, expert, but never condescending.
# Context
The user wants to write a Robot Framework test case for a specific task. They are new to the framework. The goal is to guide them to create a well-structured, modern test case using best practices.

# Rules for the Final Test Case
1.  **BEST PRACTICES**: The generated test case **MUST** use a `*** Settings ***` section to import the required library and a `*** Test Cases ***` section.
2.  **CLEAR STRUCTURE**: Use clear, human-readable keyword names.
3.  **EXPLAIN THE CODE**: After providing the code block, explain each line of the test case clearly, connecting it back to the user's goal.
4.  **PROVIDE KEYWORD DOCUMENTATION**: For each library keyword used in the solution, you **MUST** provide its official documentation and arguments, which are included below.

---
## AppiumLibrary Library Overview
AppiumLibrary is a Mobile App testing library for Robot Framework.

= Locating or specifying elements =

All keywords in AppiumLibrary that need to find an element on the page
take an argument, either a ``locator`` or a ``webelement``. ``locator``
is a string that describes how to locate an element using a syntax
specifying different location strategies. ``webelement`` is a variable that
holds a WebElement instance, which is a representation of the element.

== Using locators ==

By default, when a locator is provided, it is matched against the key attributes
of the particular element type. For iOS and Android, key attribute is ``id`` for
all elements and locating elements is easy using just the ``id``. For example:

| Click Element    id=my_element

``id`` and ``xpath`` are not required to be specified,
however ``xpath`` should start with ``//`` else just use ``xpath`` locator as explained below.

For example:

| Click Element    my_element
| Wait Until Page Contains Element    //*[@type="android.widget.EditText"]


Appium additionally supports some of the [https://w3c.github.io/webdriver/webdriver-spec.html|Mobile JSON Wire Protocol] locator strategies.
It is also possible to ...

---
## AppiumLibrary Library Keyword Reference
### `Activate Application`
**Arguments**: `app_id`
**Summary**: Activates the application if it is not running or is running in the background.
---
### `Background Application`
**Arguments**: `seconds=5`
**Summary**: Puts the application in the background on the device for a certain amount of ``seconds``.
---
### `Capture Page Screenshot`
**Arguments**: `filename=None`
**Summary**: Takes a screenshot of the current page and embeds it into the log.
---
### `Clear Text`
**Arguments**: `locator`
**Summary**: Clears the text field identified by ``locator``.
---
### `Click Alert Button`
**Arguments**: `button_name`
**Summary**: Clicks on the alert button identified by ``button_name``.
---
### `Click Element`
**Arguments**: `locator`
**Summary**: Clicks the element identified by ``locator``.
---
### `Click Text`
**Arguments**: `text, exact_match=False`
**Summary**: Clicks the text identified by ``text``.
---
### `Close All Applications`
**Arguments**: ``
**Summary**: Closes all open applications.
---
### `Close Application`
**Arguments**: ``
**Summary**: Closes the current application and the webdriver session.
---
### `Delete File`
**Arguments**: `path, timeout=5000, include_stderr=True`
**Summary**: Deletes the file specified as ``path``.
---
### `Drag And Drop`
**Arguments**: `locator, target`
**Summary**: Drags the element identified by the ``locator`` into the ``target`` element.
---
### `Element Attribute Should Match`
**Arguments**: `locator, attr_name, match_pattern, regexp=False`
**Summary**: Verifies that an attribute of an element matches the expected criteria.
---
### `Element Should Be Disabled`
**Arguments**: `locator, loglevel=INFO`
**Summary**: *DEPRECATED!!* Use `Expect Element` instead
---
### `Element Should Be Enabled`
**Arguments**: `locator, loglevel=INFO`
**Summary**: *DEPRECATED!!* Use `Expect Element` instead Verifies that the element identified by ``locator`` is enabled.
---
### `Element Should Be Visible`
**Arguments**: `locator, loglevel=INFO`
**Summary**: *DEPRECATED!!* Use `Expect Element` instead Verifies that the element identified by ``locator`` is visible.
---
### `Element Should Contain Text`
**Arguments**: `locator, expected, message`
**Summary**: Verifies the element identified by ``locator`` contains the text ``expected``.
---
### `Element Should Not Contain Text`
**Arguments**: `locator, expected, message`
**Summary**: Verifies element identified by ``locator`` does not contain the text ``expected``.
---
### `Element Text Should Be`
**Arguments**: `locator, expected, message`
**Summary**: Verifies that the element identified by ``locator`` contains the exact text ``expected``.
---
### `Execute Adb Shell`
**Arguments**: `command, args`
**Summary**: Executes ADB shell commands.
---
### `Execute Adb Shell Timeout`
**Arguments**: `command, timeout, args`
**Summary**: Executes ADB shell commands with a timeout.
---
### `Execute Async Script`
**Arguments**: `script, kwargs`
**Summary**: Injects a snippet of Async-JavaScript into the page for execution in the context of the currently selected frame (Web context only).
---
### `Execute Script`
**Arguments**: `script, kwargs`
**Summary**: Executes a variety of native, mobile commands that aren't associated with a specific endpoint. Check out the appium drivers for more details: https://appium.io/docs/en/2.19/ecosystem/drivers/.
---
### `Expect Element`
**Arguments**: `locator, state, timeout=0:00:05, retry_interval=0:00:01, message=None, loglevel=INFO`
**Summary**: Verifies that the element with the given ``locator`` has the desired ``state`` (visible, not visible, enabled, disabled.)
---
### `Expect Text`
**Arguments**: `text, state, exact_match=False, timeout=0:00:05, retry_interval=0:00:01, message=None, loglevel=INFO`
**Summary**: Verifies that the ``text`` has the desired ``state`` (visible, not visible).
---
### `Flick`
**Arguments**: `start_x, start_y, end_x, end_y`
**Summary**: Flicks from one point to another point.
---
### `Get Activity`
**Arguments**: ``
**Summary**: Retrieves the current activity on the device.
---
### `Get Appium SessionId`
**Arguments**: ``
**Summary**: Returns the current session ID as a reference.
---
### `Get Appium Timeout`
**Arguments**: ``
**Summary**: Returns the timeout in seconds used by various keywords.
---
### `Get Capability`
**Arguments**: `capability_name`
**Summary**: Returns the desired capability value by ``capability_name``.
---
### `Get Contexts`
**Arguments**: ``
**Summary**: Returns the available contexts.
---
### `Get Current Context`
**Arguments**: ``
**Summary**: Returns the current context.
---
### `Get Device Location`
**Arguments**: ``
**Summary**: Gets the device's current GPS location with human-readable address information.
---
### `Get Device Time`
**Arguments**: `format=None`
**Summary**: Returns the date and time from the device.
---
### `Get Element Attribute`
**Arguments**: `locator, attribute`
**Summary**: Returns the element attribute using the given ``attribute``, e.g. name, value, etc.
---
### `Get Element Location`
**Arguments**: `locator`
**Summary**: Returns the location of the element with the ``locator``.
---
### `Get Element Rect`
**Arguments**: `locator`
**Summary**: Returns the dimensions and coordinates of the element with the ``locator``.
---
### `Get Element Size`
**Arguments**: `locator`
**Summary**: Returns the size of the element with the ``locator``.
---
### `Get Matching Xpath Count`
**Arguments**: `xpath`
**Summary**: Returns the number of elements matching the ``xpath``
---
### `Get Network Connection Status`
**Arguments**: ``
**Summary**: Returns an integer bitmask specifying the network connection type.
---
### `Get Sleep Between Wait Loop`
**Arguments**: ``
**Summary**: Returns the sleep interval in seconds between the wait loops used by the `Wait Until ...` keywords.
---
### `Get Source`
**Arguments**: ``
**Summary**: Returns the entire source of the current page.
---
### `Get Text`
**Arguments**: `locator, first_only=True`
**Summary**: Returns the text of the element with the ``locator``.
---
### `Get Webelement`
**Arguments**: `locator`
**Summary**: Returns the first [http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement|WebElement] object matching ``locator``.
---
### `Get Webelement In Webelement`
**Arguments**: `element, locator`
**Summary**: Returns a single [http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement|WebElement] object matching ``locator`` that is a child of the argument ``element``.
---
### `Get Webelements`
**Arguments**: `locator`
**Summary**: Returns a list of [http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement|WebElement] objects matching ``locator``.
---
### `Get Window Height`
**Arguments**: ``
**Summary**: Returns the current device window height.
---
### `Get Window Title`
**Arguments**: ``
**Summary**: Returns the current Webview window title.
---
### `Get Window Url`
**Arguments**: ``
**Summary**: Returns the current Webview window URL.
---
### `Get Window Width`
**Arguments**: ``
**Summary**: Returns the current device window width.
---
### `Get Windows`
**Arguments**: ``
**Summary**: Returns the available Webview windows.
---
### `Go Back`
**Arguments**: ``
**Summary**: Goes one step backward in the browser history.
---
### `Go To Url`
**Arguments**: `url`
**Summary**: Opens the ``url`` in the default web browser.
---
### `Hide Keyboard`
**Arguments**: `key_name=None`
**Summary**: Hides the software keyboard on the device if it is currently visible.
---
### `Input Password`
**Arguments**: `locator, text`
**Summary**: Types the given password into the text field identified by ``locator``.
---
### `Input Text`
**Arguments**: `locator, text`
**Summary**: Types the given ``text`` into the text field identified by ``locator``.
---
### `Input Text Into Current Element`
**Arguments**: `text`
**Summary**: Types the given ``text`` into the currently selected text field.
---
### `Input Value`
**Arguments**: `locator, text`
**Summary**: Sets the given value into the text field identified by ``locator``. Input Value makes use of set_value.
---
### `Install App`
**Arguments**: `app_path, app_package`
**Summary**: Installs the app via appium.
---
### `Is Keyboard Shown`
**Arguments**: ``
**Summary**: Returns true or false if the device keyboard is displayed.
---
### `Landscape`
**Arguments**: ``
**Summary**: Sets the device orientation to LANDSCAPE.
---
### `Lock`
**Arguments**: `seconds=5`
**Summary**: Locks the device for a certain period of time.
---
### `Log Source`
**Arguments**: `loglevel=INFO`
**Summary**: Logs and returns the entire html source of the current page or frame.
---
### `Long Press Keycode`
**Arguments**: `keycode, metastate=None`
**Summary**: Sends a long press of ``keycode`` to the device.
---
### `Open Application`
**Arguments**: `remote_url, alias=None, kwargs`
**Summary**: Opens a new application to the given Appium server. Capabilities of appium server, Android and iOS, Please check https://appium.io/docs/en/2.19/guides/caps/ | *Option*            | *Man.* | *Description*     | | remote_url          | Yes    | Appium server url | | alias               | No     | alias             |
---
### `Open Notifications`
**Arguments**: ``
**Summary**: Opens and expands an Android device's notification drawer.
---
### `Page Should Contain Element`
**Arguments**: `locator, loglevel=INFO`
**Summary**: Verifies that the current page contains the element with the ``locator``.
---
### `Page Should Contain Text`
**Arguments**: `text, loglevel=INFO`
**Summary**: Verifies that the current page contains ``text``.
---
### `Page Should Not Contain Element`
**Arguments**: `locator, loglevel=INFO`
**Summary**: Verifies that the current page does not contain the element with the ``locator``.
---
### `Page Should Not Contain Text`
**Arguments**: `text, loglevel=INFO`
**Summary**: Verifies that the current page does not contain ``text``.
---
### `Portrait`
**Arguments**: ``
**Summary**: Sets the device orientation to PORTRAIT.
---
### `Press Keycode`
**Arguments**: `keycode, metastate=None`
**Summary**: Sends a press of ``keycode`` to the device.
---
### `Pull File`
**Arguments**: `path, decode=False`
**Summary**: Retrieves the file at ``path`` and returns its content.
---
### `Pull Folder`
**Arguments**: `path, decode=False`
**Summary**: Retrieves a folder at ``path`` and returns its zipped content.
---
### `Push File`
**Arguments**: `path, data, encode=False`
**Summary**: Puts the data in the file specified as ``path``.
---
### `Register Keyword To Run On Failure`
**Arguments**: `keyword`
**Summary**: Sets the keyword to be executed when an AppiumLibrary keyword fails.
---
### `Remove Application`
**Arguments**: `application_id`
**Summary**: Removes the application that is identified by the ``application_id``.
---
### `Scroll`
**Arguments**: `start_locator, end_locator`
**Summary**: Scrolls from the element identified by ``start_locator`` to the element identified by ``end_locator``. Key attributes for arbitrary elements are `id` and `name`. See `introduction` for details about locating elements.
---
### `Scroll Down`
**Arguments**: `locator, timeout=0:00:10, retry_interval=0:00:01`
**Summary**: Scrolls down until the element identified by ``locator`` is found or until the ``timeout`` (Android only) is reached.
---
### `Scroll Element Into View`
**Arguments**: `locator`
**Summary**: Scrolls the element with the given ``locator`` into view.
---
### `Scroll Up`
**Arguments**: `locator, timeout=0:00:10, retry_interval=0:00:01`
**Summary**: Scrolls up until the element identified by the ``locator`` is found or the ``timeout`` (Android only) is reached.
---
### `Set Appium Timeout`
**Arguments**: `seconds`
**Summary**: Sets the timeout in ``seconds`` used by various keywords.
---
### `Set Location`
**Arguments**: `latitude, longitude, altitude=10`
**Summary**: Sets the location.
---
### `Set Network Connection Status`
**Arguments**: `connectionStatus`
**Summary**: Sets the network connection status.
---
### `Set Sleep Between Wait Loop`
**Arguments**: `seconds=0.2`
**Summary**: Sets the sleep interval in ``seconds`` used by the `wait until` loop.
---
### `Shake`
**Arguments**: ``
**Summary**: Shakes the device.
---
### `Start Activity`
**Arguments**: `appPackage, appActivity, opts`
**Summary**: Starts the given activity intent. It invokes the `am start/ am start-activity` command under the hood. This keyword extends the functionality of the Start Activity app management API. The intent is built with the ``appPackage`` and ``appActivity``.
---
### `Start Screen Recording`
**Arguments**: `timeLimit=180s, options`
**Summary**: Starts an asynchronous Screen Recording for the current open application.
---
### `Stop Application`
**Arguments**: `app_id, timeout=5000, include_stderr=True`
**Summary**: Stops the app with the ``app_id`` on the device.
---
### `Stop Screen Recording`
**Arguments**: `filename=None, options`
**Summary**: Gathers the output from the previously started screen recording              to a media file, then embeds it to the log.html(Android Only).
---
### `Swipe`
**Arguments**: `, start_x, start_y, end_x, end_y, duration=0:00:01`
**Summary**: Swipes from one point to another point, for an optional ``duration``.
---
### `Swipe By Percent`
**Arguments**: `start_x, start_y, end_x, end_y, duration=0:00:01`
**Summary**: Swipes from one percent of the screen to another percent, for an optional ``duration``. Normal swipe fails to scale for different screen resolutions, this can be avoided by using this keyword.
---
### `Switch Application`
**Arguments**: `index_or_alias`
**Summary**: Switches the active application by index or alias.
---
### `Switch To Context`
**Arguments**: `context_name`
**Summary**: Switches to a new context with the ``context_name``.
---
### `Switch To Frame`
**Arguments**: `frame`
**Summary**: Switches focus to the specified ``frame``, by index, name, or webelement.
---
### `Switch To Parent Frame`
**Arguments**: ``
**Summary**: Switches focus to the parent context. If the current context is the top level browsing context, the context remains unchanged.
---
### `Switch To Window`
**Arguments**: `window_name`
**Summary**: Switches to a new webview window with the ``window_name`` if the application contains multiple webviews.
---
### `Tap`
**Arguments**: `element, count=1, duration=0:00:01`
**Summary**: Taps the ``element`` for ``count`` times over the ``duration``. 
---
### `Tap With Number Of Taps`
**Arguments**: `locator, number_of_taps, number_of_touches`
**Summary**: Sends one or more taps with one or more touch points.
---
### `Tap With Positions`
**Arguments**: `duration=0:00:00.500000, locations`
**Summary**: Taps on a particular place with up to five fingers, holding for a certain time.
---
### `Terminate Application`
**Arguments**: `app_id`
**Summary**: Terminates the given app on the device.
---
### `Text Should Be Visible`
**Arguments**: `text, exact_match=False, loglevel=INFO`
**Summary**: *DEPRECATED!!* Use `Expect Text` instead Verifies that the element identified by ``text`` is visible.
---
### `Toggle Touch Id Enrollment`
**Arguments**: ``
**Summary**: Toggles Touch ID enrolled state on the iOS Simulator.
---
### `Touch Id`
**Arguments**: `match=True`
**Summary**: Simulates Touch ID on the iOS Simulator.`
---
### `Wait Activity`
**Arguments**: `activity, timeout, interval=1`
**Summary**: Waits for an activity: blocks until target activity presents or until the timeout is reached.
---
### `Wait Until Element Is Visible`
**Arguments**: `locator, timeout=None, error=None`
**Summary**: Waits until the element specified by the ``locator`` is visible.
---
### `Wait Until Page Contains`
**Arguments**: `text, timeout=None, error=None`
**Summary**: Waits until the ``text`` appears on the current page.
---
### `Wait Until Page Contains Element`
**Arguments**: `locator, timeout=None, error=None`
**Summary**: Waits until the element specified by the ``locator`` appears on the current page.
---
### `Wait Until Page Does Not Contain`
**Arguments**: `text, timeout=None, error=None`
**Summary**: Waits until the ``text`` disappears from the current page.
---
### `Wait Until Page Does Not Contain Element`
**Arguments**: `locator, timeout=None, error=None`
**Summary**: Waits until the element specified by the ``locator`` disappears from the current page.
---
### `Xpath Should Match X Times`
**Arguments**: `xpath, count, error=None, loglevel=INFO`
**Summary**: Verifies that the page contains the given number of elements (``count``) located by ``xpath``.
---

---
## BuiltIn Library Keyword Reference
The `BuiltIn` library is part of the Robot Framework core and its keywords are always available.
### `Call Method`
**Arguments**: `object, method_name, args, kwargs`
**Summary**: Calls the named method of the given object with the provided arguments.
---
### `Catenate`
**Arguments**: `items`
**Summary**: Catenates the given items together and returns the resulted string.
---
### `Comment`
**Arguments**: `messages`
**Summary**: Displays the given messages in the log file as keyword arguments.
---
### `Continue For Loop`
**Arguments**: ``
**Summary**: Skips the current FOR loop iteration and continues from the next.
---
### `Continue For Loop If`
**Arguments**: `condition`
**Summary**: Skips the current FOR loop iteration if the ``condition`` is true.
---
### `Convert To Binary`
**Arguments**: `item, base=None, prefix=None, length=None`
**Summary**: Converts the given item to a binary string.
---
### `Convert To Boolean`
**Arguments**: `item`
**Summary**: Converts the given item to Boolean ``True`` or ``False``.
---
### `Convert To Bytes`
**Arguments**: `input, input_type=text`
**Summary**: Converts the given ``input`` to bytes according to the ``input_type``.
---
### `Convert To Hex`
**Arguments**: `item, base=None, prefix=None, length=None, lowercase=False`
**Summary**: Converts the given item to a hexadecimal string.
---
### `Convert To Integer`
**Arguments**: `item, base=None`
**Summary**: Converts the given item to an integer number.
---
### `Convert To Number`
**Arguments**: `item, precision=None`
**Summary**: Converts the given item to a floating point number.
---
### `Convert To Octal`
**Arguments**: `item, base=None, prefix=None, length=None`
**Summary**: Converts the given item to an octal string.
---
### `Convert To String`
**Arguments**: `item`
**Summary**: Converts the given item to a Unicode string.
---
### `Create Dictionary`
**Arguments**: `items`
**Summary**: Creates and returns a dictionary based on the given ``items``.
---
### `Create List`
**Arguments**: `items`
**Summary**: Returns a list containing given items.
---
### `Evaluate`
**Arguments**: `expression, modules=None, namespace=None`
**Summary**: Evaluates the given expression in Python and returns the result.
---
### `Exit For Loop`
**Arguments**: ``
**Summary**: Stops executing the enclosing FOR loop.
---
### `Exit For Loop If`
**Arguments**: `condition`
**Summary**: Stops executing the enclosing FOR loop if the ``condition`` is true.
---
### `Fail`
**Arguments**: `msg=None, tags`
**Summary**: Fails the test with the given message and optionally alters its tags.
---
### `Fatal Error`
**Arguments**: `msg=None`
**Summary**: Stops the whole test execution.
---
### `Get Count`
**Arguments**: `container, item`
**Summary**: Returns and logs how many times ``item`` is found from ``container``.
---
### `Get Length`
**Arguments**: `item`
**Summary**: Returns and logs the length of the given item as an integer.
---
### `Get Library Instance`
**Arguments**: `name=None, all=False`
**Summary**: Returns the currently active instance of the specified library.
---
### `Get Time`
**Arguments**: `format=timestamp, time_=NOW`
**Summary**: Returns the given time in the requested format.
---
### `Get Variable Value`
**Arguments**: `name, default=None`
**Summary**: Returns variable value or ``default`` if the variable does not exist.
---
### `Get Variables`
**Arguments**: `no_decoration=False`
**Summary**: Returns a dictionary containing all variables in the current scope.
---
### `Import Library`
**Arguments**: `name, args`
**Summary**: Imports a library with the given name and optional arguments.
---
### `Import Resource`
**Arguments**: `path`
**Summary**: Imports a resource file with the given path.
---
### `Import Variables`
**Arguments**: `path, args`
**Summary**: Imports a variable file with the given path and optional arguments.
---
### `Keyword Should Exist`
**Arguments**: `name, msg=None`
**Summary**: Fails unless the given keyword exists in the current scope.
---
### `Length Should Be`
**Arguments**: `item, length, msg=None`
**Summary**: Verifies that the length of the given item is correct.
---
### `Log`
**Arguments**: `message, level=INFO, html=False, console=None, repr=DEPRECATED, formatter=str`
**Summary**: Logs the given message with the given level.
---
### `Log Many`
**Arguments**: `messages`
**Summary**: Logs the given messages as separate entries using the INFO level.
---
### `Log To Console`
**Arguments**: `message, stream=stdout, no_newline=False, format=None`
**Summary**: Logs the given message to the console.
---
### `Log Variables`
**Arguments**: `level=INFO`
**Summary**: Logs all variables in the current scope with given log level.
---
### `No Operation`
**Arguments**: ``
**Summary**: Does absolutely nothing.
---
### `Pass Execution`
**Arguments**: `message, tags`
**Summary**: Skips rest of the current test, setup, or teardown with PASS status.
---
### `Pass Execution If`
**Arguments**: `condition, message, tags`
**Summary**: Conditionally skips rest of the current test, setup, or teardown with PASS status.
---
### `Regexp Escape`
**Arguments**: `patterns`
**Summary**: Returns each argument escaped for use as a regular expression.
---
### `Reload Library`
**Arguments**: `name_or_instance`
**Summary**: Rechecks what keywords the specified library provides.
---
### `Remove Tags`
**Arguments**: `tags`
**Summary**: Removes given ``tags`` from the current test or all tests in a suite.
---
### `Repeat Keyword`
**Arguments**: `repeat, name, , args`
**Summary**: Executes the specified keyword multiple times.
---
### `Replace Variables`
**Arguments**: `text`
**Summary**: Replaces variables in the given text with their current values.
---
### `Reset Log Level`
**Arguments**: ``
**Summary**: Resets the log level to the original value.
---
### `Return From Keyword`
**Arguments**: `return_values`
**Summary**: Returns from the enclosing user keyword.
---
### `Return From Keyword If`
**Arguments**: `condition, return_values`
**Summary**: Returns from the enclosing user keyword if ``condition`` is true.
---
### `Run Keyword`
**Arguments**: `name, , args`
**Summary**: Executes the given keyword with the given arguments.
---
### `Run Keyword And Continue On Failure`
**Arguments**: `name, , args`
**Summary**: Runs the keyword and continues execution even if a failure occurs.
---
### `Run Keyword And Expect Error`
**Arguments**: `expected_error, name, , args`
**Summary**: Runs the keyword and checks that the expected error occurred.
---
### `Run Keyword And Ignore Error`
**Arguments**: `name, , args`
**Summary**: Runs the given keyword with the given arguments and ignores possible error.
---
### `Run Keyword And Return`
**Arguments**: `name, , args`
**Summary**: Runs the specified keyword and returns from the enclosing user keyword.
---
### `Run Keyword And Return If`
**Arguments**: `condition, name, , args`
**Summary**: Runs the specified keyword and returns from the enclosing user keyword.
---
### `Run Keyword And Return Status`
**Arguments**: `name, , args`
**Summary**: Runs the specified keyword and returns the status as a Boolean value.
---
### `Run Keyword And Warn On Failure`
**Arguments**: `name, , args`
**Summary**: Runs the specified keyword logs a warning if the keyword fails.
---
### `Run Keyword If`
**Arguments**: `condition, name, , args`
**Summary**: Runs the given keyword with the given arguments, if ``condition`` is true.
---
### `Run Keyword If All Tests Passed`
**Arguments**: `name, , args`
**Summary**: Runs the given keyword with the given arguments, if all tests passed.
---
### `Run Keyword If Any Tests Failed`
**Arguments**: `name, , args`
**Summary**: Runs the given keyword with the given arguments, if one or more tests failed.
---
### `Run Keyword If Test Failed`
**Arguments**: `name, , args`
**Summary**: Runs the given keyword with the given arguments, if the test failed.
---
### `Run Keyword If Test Passed`
**Arguments**: `name, , args`
**Summary**: Runs the given keyword with the given arguments, if the test passed.
---
### `Run Keyword If Timeout Occurred`
**Arguments**: `name, , args`
**Summary**: Runs the given keyword if either a test or a keyword timeout has occurred.
---
### `Run Keyword Unless`
**Arguments**: `condition, name, , args`
**Summary**: *DEPRECATED since RF 5.0. Use native IF/ELSE or `Run Keyword If` instead.*
---
### `Run Keywords`
**Arguments**: `names_and_args`
**Summary**: Executes all the given keywords in a sequence.
---
### `Set Global Variable`
**Arguments**: `name, , values`
**Summary**: Makes a variable available globally in all tests and suites.
---
### `Set Library Search Order`
**Arguments**: `search_order`
**Summary**: Sets the resolution order to use when a name matches multiple keywords.
---
### `Set Local Variable`
**Arguments**: `name, , values`
**Summary**: Makes a variable available everywhere within the local scope.
---
### `Set Log Level`
**Arguments**: `level`
**Summary**: Sets the log threshold to the specified level.
---
### `Set Suite Documentation`
**Arguments**: `doc, append=False, top=False, separator=\ \`
**Summary**: Sets documentation for the current test suite.
---
### `Set Suite Metadata`
**Arguments**: `name, value, append=False, top=False, separator=\ \`
**Summary**: Sets metadata for the current test suite.
---
### `Set Suite Variable`
**Arguments**: `name, , values`
**Summary**: Makes a variable available everywhere within the scope of the current suite.
---
### `Set Tags`
**Arguments**: `tags`
**Summary**: Adds given ``tags`` for the current test or all tests in a suite.
---
### `Set Task Variable`
**Arguments**: `name, , values`
**Summary**: Makes a variable available everywhere within the scope of the current task.
---
### `Set Test Documentation`
**Arguments**: `doc, append=False, separator=\ \`
**Summary**: Sets documentation for the current test case.
---
### `Set Test Message`
**Arguments**: `message, append=False, separator=\ \`
**Summary**: Sets message for the current test case.
---
### `Set Test Variable`
**Arguments**: `name, , values`
**Summary**: Makes a variable available everywhere within the scope of the current test.
---
### `Set Variable`
**Arguments**: `values`
**Summary**: Returns the given values which can then be assigned to a variables.
---
### `Set Variable If`
**Arguments**: `condition, , values`
**Summary**: Sets variable based on the given condition.
---
### `Should Be Empty`
**Arguments**: `item, msg=None`
**Summary**: Verifies that the given item is empty.
---
### `Should Be Equal`
**Arguments**: `first, second, msg=None, values=True, ignore_case=False, formatter=str, strip_spaces=False, collapse_spaces=False, type=None, types=None`
**Summary**: Fails if the given objects are unequal.
---
### `Should Be Equal As Integers`
**Arguments**: `first, second, msg=None, values=True, base=None`
**Summary**: Fails if objects are unequal after converting them to integers.
---
### `Should Be Equal As Numbers`
**Arguments**: `first, second, msg=None, values=True, precision=6`
**Summary**: Fails if objects are unequal after converting them to real numbers.
---
### `Should Be Equal As Strings`
**Arguments**: `first, second, msg=None, values=True, ignore_case=False, strip_spaces=False, formatter=str, collapse_spaces=False`
**Summary**: Fails if objects are unequal after converting them to strings.
---
### `Should Be True`
**Arguments**: `condition, msg=None`
**Summary**: Fails if the given condition is not true.
---
### `Should Contain`
**Arguments**: `container, item, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if ``container`` does not contain ``item`` one or more times.
---
### `Should Contain Any`
**Arguments**: `container, items, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if ``container`` does not contain any of the ``*items``.
---
### `Should Contain X Times`
**Arguments**: `container, item, count, msg=None, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if ``container`` does not contain ``item`` ``count`` times.
---
### `Should End With`
**Arguments**: `str1, str2, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if the string ``str1`` does not end with the string ``str2``.
---
### `Should Match`
**Arguments**: `string, pattern, msg=None, values=True, ignore_case=False`
**Summary**: Fails if the given ``string`` does not match the given ``pattern``.
---
### `Should Match Regexp`
**Arguments**: `string, pattern, msg=None, values=True, flags=None`
**Summary**: Fails if ``string`` does not match ``pattern`` as a regular expression.
---
### `Should Not Be Empty`
**Arguments**: `item, msg=None`
**Summary**: Verifies that the given item is not empty.
---
### `Should Not Be Equal`
**Arguments**: `first, second, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if the given objects are equal.
---
### `Should Not Be Equal As Integers`
**Arguments**: `first, second, msg=None, values=True, base=None`
**Summary**: Fails if objects are equal after converting them to integers.
---
### `Should Not Be Equal As Numbers`
**Arguments**: `first, second, msg=None, values=True, precision=6`
**Summary**: Fails if objects are equal after converting them to real numbers.
---
### `Should Not Be Equal As Strings`
**Arguments**: `first, second, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if objects are equal after converting them to strings.
---
### `Should Not Be True`
**Arguments**: `condition, msg=None`
**Summary**: Fails if the given condition is true.
---
### `Should Not Contain`
**Arguments**: `container, item, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if ``container`` contains ``item`` one or more times.
---
### `Should Not Contain Any`
**Arguments**: `container, items, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if ``container`` contains one or more of the ``*items``.
---
### `Should Not End With`
**Arguments**: `str1, str2, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if the string ``str1`` ends with the string ``str2``.
---
### `Should Not Match`
**Arguments**: `string, pattern, msg=None, values=True, ignore_case=False`
**Summary**: Fails if the given ``string`` matches the given ``pattern``.
---
### `Should Not Match Regexp`
**Arguments**: `string, pattern, msg=None, values=True, flags=None`
**Summary**: Fails if ``string`` matches ``pattern`` as a regular expression.
---
### `Should Not Start With`
**Arguments**: `str1, str2, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if the string ``str1`` starts with the string ``str2``.
---
### `Should Start With`
**Arguments**: `str1, str2, msg=None, values=True, ignore_case=False, strip_spaces=False, collapse_spaces=False`
**Summary**: Fails if the string ``str1`` does not start with the string ``str2``.
---
### `Skip`
**Arguments**: `msg=Skipped with Skip keyword.`
**Summary**: Skips the rest of the current test.
---
### `Skip If`
**Arguments**: `condition, msg=None`
**Summary**: Skips the rest of the current test if the ``condition`` is True.
---
### `Sleep`
**Arguments**: `time_, reason=None`
**Summary**: Pauses the test executed for the given time.
---
### `Variable Should Exist`
**Arguments**: `name, message=None`
**Summary**: Fails unless the given variable exists within the current scope.
---
### `Variable Should Not Exist`
**Arguments**: `name, message=None`
**Summary**: Fails if the given variable exists within the current scope.
---
### `Wait Until Keyword Succeeds`
**Arguments**: `retry, retry_interval, name, , args`
**Summary**: Runs the specified keyword and retries if it fails.
---

# Task
You will guide a new user to create a Robot Framework test case for a mobile application, helping them identify locators.

Your conversation plan is similar to web testing but focused on mobile:
1.  Ask for the user's goal (e.g., "I want to open my app, tap the login button, and type in a username").
2.  Ask for key information: **Platform** (iOS or Android), **App Path/Identifier**, and descriptions of the **Elements** to interact with.
3.  Teach the user how to find a locator for **one** element using **Appium Inspector**. Explain that `accessibility id` is often the best and most reliable locator.
4.  Generate the complete `.robot` file, using the found locator and placeholders for the others.

Your final response after gathering information MUST contain the code, an explanation, and keyword references.
