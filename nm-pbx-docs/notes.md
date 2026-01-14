# Notes

Record information here that will be useful for future instances of AI agents and human developers when working on the rebranding and customisations for the "NM PBX" project.

## Rebranding Overview

This document tracks the changes needed to rebrand Linphone Desktop to "NM PBX".

### Files Modified

1. **`linphone-app/application_info.cmake`** - Application name, vendor, URL, description
2. **`linphone-app/src/utils/Constants.hpp`** - Logo path, font name, URLs
3. **`linphone-app/src/components/other/colors/ColorListModel.hpp`** - Color definitions
4. **`linphone-app/resources.qrc`** - Asset registration (fonts, images)
5. **`linphone-app/ui/views/App/Main/Dialogs/About.qml`** - Logo icon reference
6. **`linphone-app/assets/languages/en.ts`** - English translations

### Brand Colors Applied

- **Primary (`#25af4b`)** - Green - replaces Linphone orange (`#FF5E00`)
- **Secondary (`#0e2826`)** - Dark green/teal
- **Gradient end (`#a4cd3a`)** - Light green for gradients

### Font Change

- Changed from "Noto Sans" to "Poppins"
- Poppins font files need to be added to `linphone-app/assets/fonts/Poppins/`
- Required weights: Light (body), Medium (subtitles), Bold (titles)

### Logo Files

NM PBX logos available in `linphone-app/assets/images/`:
- `NMPBX_NMPBX_Main_Logo.svg` - Primary logo
- `NMPBX_NMPBX_Black_Logo.svg` - Black variant
- `NMPBX_NMPBX_White_Logo.svg` - White variant
- `NMPBX_NMPBX_White_and_Green_Logo.svg` - White/green variant
- `NMPBX_X_Isolated.svg` - Standalone X icon
- `NMPBX_X_Isolated_Black.svg` - Black X icon
- `NMPBX_X_Isolated_White.svg` - White X icon

---

## Linphone API Integrations Requiring Attention

These are Linphone-specific service endpoints and configurations that will need updating for a complete white-label deployment:

### Critical - SIP Infrastructure (Constants.hpp)

These URLs point to Linphone's servers and MUST be changed for production:

1. **`DefaultXmlrpcUri`** - `https://subscribe.linphone.org:444/wizard.php`
   - Account creation wizard API

2. **`DefaultFlexiAPIURL`** - `https://subscribe.linphone.org/api/`
   - Flexi API for account management

3. **`RemoteProvisioningURL`** - `https://subscribe.linphone.org/api/provisioning`
   - Remote configuration provisioning

4. **`DefaultRlsUri`** - `sips:rls@sip.linphone.org`
   - Presence/Resource List Server

5. **`DefaultConferenceURI`** - `sip:conference-factory@sip.linphone.org`
   - Audio conference factory

6. **`DefaultVideoConferenceURI`** - `sip:videoconference-factory@sip.linphone.org`
   - Video conference factory

7. **`DefaultLimeServerURL`** - `https://lime.linphone.org/lime-server/lime-server.php`
   - End-to-end encryption (LIME) server

8. **`DefaultRouteAddress`** - `sip:sip.linphone.org;transport=tls`
   - Default SIP routing

### Medium Priority - Support & Updates

9. **`DefaultUploadLogsServer`** - `https://files.linphone.org/http-file-transfer-server/hft.php`
   - Log upload for debugging

10. **`DownloadUrl`** - `https://www.linphone.org/en/technical-corner/linphone`
    - Application download page

11. **`VersionCheckReleaseUrl`** - `https://download.linphone.org/releases`
    - Update check URL (releases)

12. **`VersionCheckNightlyUrl`** - `https://download.linphone.org/snapshots`
    - Update check URL (nightlies)

13. **`DefaultLogsEmail`** - `linphone-desktop@belledonne-communications.com`
    - Support email address

### Low Priority - Legal & Account Management

14. **`PasswordRecoveryUrl`** - `https://subscribe.linphone.org/recovery/email`
    - Password recovery page

15. **`CguUrl`** - `https://www.linphone.org/en/terms-of-use`
    - Terms of use

16. **`PrivatePolicyUrl`** - `https://linphone.org/en/privacy-policy`
    - Privacy policy

17. **`ContactUrl`** - `https://www.linphone.org/en/contact`
    - Contact page

18. **`TranslationUrl`** - `https://weblate.linphone.org/projects/linphone/linphone-desktop-6-0/`
    - Translation contribution page

### Assistant/WebView URLs

19. **`DefaultAssistantRegistrationUrl`** - `https://subscribe.linphone.org/register`
20. **`DefaultAssistantLoginUrl`** - `https://subscribe.linphone.org/login`
21. **`DefaultAssistantLogoutUrl`** - `https://subscribe.linphone.org/logout`

### Domain Detection

22. **`LinphoneDomain`** - `sip.linphone.org`
    - Used to detect if an account is a Linphone account (for special handling)

### OAuth2 Settings (Currently Empty)

The OAuth2 settings in Constants.hpp are currently empty placeholders:
- `OAuth2AuthorizationUrl`
- `OAuth2AccessTokenUrl`
- `OAuth2RedirectUri`
- `OAuth2Identifier`
- `OAuth2Password`
- `OAuth2Scope`

These would need to be configured if using OAuth2 authentication.

---

## Factory Configuration

The file `linphone-app/assets/linphonerc-factory` contains default SIP configuration that may need adjustment for your SIP infrastructure.

---

## Database Files

The application creates these database files (paths defined in Constants.hpp):
- `linphonerc` - Main configuration
- `linphone.db` - Main database
- `call-history.db` - Call history
- `message-history.db` - Message history
- `friends.db` - Contacts
- `x3dh.c25519.sqlite3` - LIME encryption keys
- `zidcache` - ZRTP secrets

---

## Build Notes

- The application uses Qt 5 (minimum 5.13)
- CMake is used for building
- The Linphone SDK is included as a submodule in `linphone-sdk/`
- Windows build outputs to `CMAKE_CURRENT_BINARY_DIR`

---

## Completed Rebranding Changes

The following changes have been made as part of the NM PBX rebranding:

### 1. Application Identity (`application_info.cmake`)
- `APPLICATION_NAME`: "NM PBX"
- `APPLICATION_ID`: "uk.co.netmatters.nmpbx"
- `APPLICATION_DESCRIPTION`: "NM PBX Desktop Client"
- `APPLICATION_URL`: "https://www.netmatters.co.uk/"
- `APPLICATION_VENDOR`: "Netmatters"
- `APPLICATION_START_LICENCE`: "2025"
- `EXECUTABLE_NAME`: "nmpbx"

### 2. Visual Identity (`Constants.hpp`)
- `DefaultFont`: Changed from "Noto Sans" to "Poppins"
- `WindowIconPath`: Changed to NM PBX main logo
- `ContactUrl`: Changed to Netmatters contact page
- `TranslationUrl`: Cleared (empty string) - no external translation contribution page

### 3. Color Scheme (`ColorListModel.hpp`)
- Primary color (`i`): `#25af4b` (NM PBX green, was orange `#FF5E00`)
- Outgoing message background: `#E5F5EA` (light green tint)
- Outgoing reply mark: `#6BC77E` (green variant)
- In-call message banner: `#0e2826` (NM PBX secondary dark)

### 4. Assets (`resources.qrc`)
- Added NM PBX logo SVG files to resource bundle
- Added Poppins font files to resource bundle (files need to be downloaded)

### 5. UI Components (`About.qml`)
- Updated logo reference from `linphone_logo` to `NMPBX_NMPBX_Main_Logo`

### 6. Translations (`en.ts`)
- Updated `applicationDescription` to "NM PBX Desktop Client - A SIP video-phone provided by Netmatters."

### 7. Windows Application Icon (`assets/icon.ico`)
- Generated new Windows executable icon from `nm-pbx-logo-256.png`
- Updated icon generation script (`assets/icons/genicons.sh`) to use NM PBX logo
- Created Python helper script (`assets/icons/generate_ico.py`) for icon generation

---

## Remaining Manual Steps

1. **Configure SIP Infrastructure**: Update the Linphone API URLs in `Constants.hpp` to point to your own SIP infrastructure (see "Linphone API Integrations Requiring Attention" section above)

2. **Build and Test**: Rebuild the application and verify all branding changes appear correctly
   - After rebuilding, the new NM PBX icon should appear in the window title bar and as the executable icon
   - If the old icon persists, try a clean rebuild (delete build directory) and clear Windows icon cache

