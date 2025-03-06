
# Selenium Chrome Options

## Explanation of Added Arguments
--headless: Runs Chrome without displaying the browser window.  
--disable-gpu: Turns off GPU hardware acceleration to avoid issues in headless mode. Particularly useful on Windows; Linux doesn't always require this.  
--no-sandbox: Bypasses Chrome's security model to avoid permission issues, mainly in certain environments like Docker. More common in Linux environments.  
--disable-dev-shm-usage: Avoids using shared memory, useful for environments with limited resources, such as some CI servers and Docker containers. Often needed on Linux.  
--log-level=3: Suppresses all logs except for fatal errors.  
--disable-extensions: Turns off all browser extensions.  
--disable-popup-blocking: Prevents Chrome from blocking pop-up windows.  
--disable-notifications: Stops web notifications from appearing.  
--disable-infobars: Hides the message that says "Chrome is being controlled by automated test software".  
--start-maximized: Starts Chrome maximized to avoid issues with window sizes.  
--window-size=1920x1080: Sets the initial window size. Useful in headless mode to define screen resolution.  
--incognito: Opens Chrome in incognito mode.  
--disable-web-security: Disables same-origin policy. Not recommended for production use.  
--user-agent=YOUR_USER_AGENT: Sets a custom user agent string.  
--remote-debugging-port=9222: Enables remote debugging.  
--ignore-certificate-errors: Ignores certificate errors (useful for testing with self-signed certificates).  
--allow-running-insecure-content: Allows loading of insecure content (HTTP) on secure sites (HTTPS).  
--disable-software-rasterizer: Disables the use of a software rasterizer.  
--disable-setuid-sandbox: Disables the setuid sandbox (useful in some Linux environments).  
--disable-background-networking: Disables several background networking services.  
--disable-background-timer-throttling: Disables background timer throttling.  
--disable-backgrounding-occluded-windows: Disables backgrounding of occluded windows.  
--disable-breakpad: Disables the crash reporting.  
--disable-client-side-phishing-detection: Disables client-side phishing detection.  
--disable-component-extensions-with-background-pages: Disables component extensions with background pages.  
--disable-default-apps: Disables default apps on first run.  
--disable-domain-reliability: Disables domain reliability monitoring.  
--disable-features=FEATURES: Disables specified features.  
--disable-hang-monitor: Disables the hang monitor.  
--disable-ipc-flooding-protection: Disables IPC flooding protection.  
--disable-offer-store-unmasked-wallet-cards: Disables offering to store unmasked wallet cards.  
--disable-print-preview: Disables print preview.  
--disable-prompt-on-repost: Disables the prompt on repost.  
--disable-renderer-backgrounding: Disables renderer backgrounding.  
--disable-sync: Disables syncing to a Google account.  
--disable-translate: Disables the Translate feature.  
--metrics-recording-only: Enables metrics recording only.  
--no-first-run: Disables the first run experience.  
--password-store=basic: Uses basic password store.  
--use-mock-keychain: Uses mock keychain (useful for testing on macOS).  

## Differences Between Running on Windows and Linux
1. **--disable-gpu**:
   - **Windows**: Often necessary to avoid issues in headless mode.
   - **Linux**: Not always required; can sometimes be omitted.

2. **--no-sandbox** and **--disable-setuid-sandbox**:
   - **Windows**: Generally not required.
   - **Linux**: Commonly used in containerized environments like Docker to avoid permission issues.

3. **--disable-dev-shm-usage**:
   - **Windows**: Not typically needed.
   - **Linux**: Useful to avoid shared memory issues, especially in CI environments.

4. **File Paths**:
   - **Windows**: Uses backslashes (e.g., `C:\path\to\chromedriver.exe`).
   - **Linux**: Uses forward slashes (e.g., `/usr/local/bin/chromedriver`).

5. **Environment Variables**:
   - **Windows**: Path variables might need to be set differently.
   - **Linux**: Generally uses straightforward path settings.
