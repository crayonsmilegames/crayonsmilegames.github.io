"""Reviewed policy copy, aligned with local app behavior on 2026-10-28."""
EFFECTIVE = '2026-10-28'
APP_DATA = {
    'somi-kids-world': [
        '학습·놀이 진도, 언어·음량 설정, 색칠·스티커 작품, 보호자가 녹음한 시작 인사·동화책 음성. 카메라 놀이를 사용하면 카메라 화면, 선택한 사진과 꾸민 사진을 기기에서 처리합니다.',
        'Learning and play progress, language and sound settings, coloring and sticker creations, and greetings or storybook narration recorded by a guardian. Camera play processes the camera preview, selected pictures and decorated photos on the device.'
    ],
    'hangul-abc': [
        '프로필에 입력한 이름 또는 별명, 나이, 선택한 아바타, 학습·복습 결과, 읽은 이야기와 설정. 내 이름 글자 놀이와 프로필별 진도 제공에 이용하며 기기의 앱 저장 공간에 저장합니다.',
        'The name or nickname and age entered in a local profile, selected avatar, learning and review results, reading progress and settings. These support name-based letter activities and profile-specific progress and are saved in app storage on the device.'
    ],
    'somi-flashcards': [
        '학습 언어, 만난 낱말, 정답·재도전 기록, 경험치와 카드·마을 진행 상태, 설정과 콘텐츠 이용 권한. 카드 기울임 효과에는 기기의 중력 센서 입력을 사용합니다. 학습 기록은 기기에 저장하고 센서 입력은 기기에서 처리하며 온라인 분석 서버로 전송하지 않습니다.',
        'Learning language, encountered words, answer and retry records, experience and card or village progress, settings and content entitlements. Card tilt effects use the device’s gravity sensor input. Learning records stay on the device, sensor input is processed on the device, and neither is sent to an online analytics server.'
    ],
    'somi-coloring': [
        '선택한 도안, 색상·브러시 등 도구 설정과 색칠 화면을 기기에서 처리합니다. 이 앱은 카메라 촬영이나 가족 음성 녹음 기능을 제공하지 않습니다.',
        'Selected templates, color and brush settings, and the coloring canvas are processed on the device. This app does not provide camera capture or family voice recording.'
    ]
}

# Each paragraph is authored as bilingual HTML. Keep the two versions aligned.
SECTIONS = [
    ('scope', ['1. 적용 범위와 운영자', '1. Scope and operator'], [
        ['CrayonSmile(크레용스마일)은 어린이와 가족을 위한 게임을 만드는 대한민국 개인사업자입니다. 이 방침은 아래 네 앱과 이 공식 웹사이트에 적용됩니다. 출시 예정 앱은 현재 개발 중인 기능을 기준으로 안내하며, 기능이나 처리 방식이 바뀌면 이 방침을 갱신합니다.',
         'CrayonSmile is a Korean sole proprietorship creating games for children and families. This policy covers the four apps below and this official website. Information about upcoming apps describes their current development features; we will update this policy if those features or data practices change.'],
        ['앱에는 CrayonSmile 온라인 회원가입이나 사용자 계정 서버가 없습니다. 학습을 위해 기기에서 정보를 입력·처리하는 것과 운영자가 서버로 정보를 수집하는 것은 구분됩니다. 아래 로컬 데이터는 앱이 CrayonSmile 서버로 업로드하지 않습니다.',
         'The apps have no CrayonSmile online sign-up or user account server. Information entered and processed locally for learning is distinct from information collected by an operator on a server. The apps do not upload the local data described below to a CrayonSmile server.']
    ]),
    ('local-data', ['2. 앱별로 기기에서 처리하는 정보', '2. Information processed on the device'], [
        ['앱별로 사용하는 정보와 목적은 다음과 같습니다. 모든 앱이 같은 기능이나 같은 정보를 사용하는 것은 아닙니다.',
         'The information and purposes differ by app. A feature or data type listed for one app is not automatically used by the other apps.']
    ]),
    ('voice', ['3. 보호자·가족 내레이션 녹음', '3. Guardian and family narration'], [
        ['소미 키즈월드의 녹음은 보호자가 자신의 목소리로 시작 인사나 동화책 내레이션·등장인물 대사를 만드는 기능입니다. 아동 음성 수집, 음성 인식, 전사, 화자 식별이나 음성 복제 서비스가 아닙니다.',
         'Recording in Somi Kids World lets a guardian record their own voice for greetings, storybook narration and character dialogue. It is not a service for collecting children’s voices, speech recognition, transcription, speaker identification or voice cloning.'],
        ['녹음은 보호자가 녹음 조작을 시작했을 때 사용하며 파일은 기기의 앱 저장 공간에 보관합니다. 앱이 녹음 파일을 업로드하거나 원격 저장·분석하지 않습니다. 보호자 녹음 관리에서 개별 녹음을 삭제할 수 있습니다.',
         'Recording is used when a guardian starts a recording action. Files stay in app storage on the device; the app does not upload, remotely store or analyze them. Individual recordings can be deleted in guardian recording management.']
    ]),
    ('camera', ['4. 카메라 놀이와 사진', '4. Camera play and photos'], [
        ['소미 키즈월드의 카메라 놀이는 카메라 미리보기와 스티커·효과를 넣은 사진 꾸미기를 제공합니다. 효과 위치를 맞추기 위한 얼굴 위치·특징점은 기기에서 처리합니다. 사람의 신원을 판별하거나 얼굴 인식용 프로필·생체인식 템플릿을 만들지 않으며, 카메라 영상과 얼굴 위치 정보를 서버로 전송하지 않습니다.',
         'Camera play in Somi Kids World provides a camera preview and photo decoration with stickers and effects. Face positions and landmarks used to place effects are processed on the device. The app does not identify people or create identity-recognition profiles or biometric templates, and does not send camera frames or face-position data to a server.'],
        ['기존 사진은 시스템 사진 선택기에서 사용자가 고른 사진만 가져옵니다. 전체 사진첩을 스캔하지 않습니다. 사용자가 사진을 저장하면 Android 갤러리의 <strong>Pictures/Somi Kids World</strong>에 저장합니다. 앱 자체는 소셜 공유·사진 업로드·클라우드 백업을 제공하지 않습니다.',
         'For an existing picture, the app receives only the picture chosen through the system photo picker; it does not scan the whole photo library. When a user saves a photo, it is placed in <strong>Pictures/Somi Kids World</strong> in the Android gallery. The app itself provides no social sharing, photo upload or cloud backup.'],
        ['갤러리에 저장한 사진은 앱을 삭제해도 남을 수 있습니다. 갤러리 앱에서 별도로 삭제해 주세요. 기기의 사진 백업·공유 서비스를 켜둔 경우 해당 서비스가 사진을 처리할 수 있으며, 이는 사용자의 기기 설정과 그 서비스의 정책에 따릅니다.',
         'Photos saved to the gallery may remain after uninstalling the app. Delete them separately in the gallery. If device photo backup or sharing services are enabled, those services may process the pictures under your device settings and their own policies.']
    ]),
    ('permissions', ['5. 권한과 보호자의 선택', '5. Permissions and guardian choices'], [
        ['소미 키즈월드는 카메라 놀이를 위해 카메라 권한을, 보호자 녹음을 위해 마이크 권한을 사용합니다. 현재 버전은 최초 실행 안내 뒤 또는 해당 기능을 시작할 때 권한을 요청할 수 있습니다. 권한 허용만으로 녹음을 시작하거나 백그라운드 촬영·녹음을 수행하지 않습니다.',
         'Somi Kids World uses camera permission for camera play and microphone permission for guardian recordings. The current version may ask after the first-launch introduction or when entering the relevant feature. Granting permission alone does not start recording, and the app does not perform background camera capture or audio recording.'],
        ['권한은 거부할 수 있으며 Android의 설정 → 앱 → 해당 앱 → 권한에서 변경할 수 있습니다. 권한이 필요한 기능은 제한될 수 있지만, 권한을 사용하지 않는 놀이를 위해 이를 허용할 필요는 없습니다. 다른 세 앱은 현재 카메라·마이크를 이용하는 기능을 제공하지 않습니다.',
         'You can decline permissions or change them in Android Settings → Apps → the app → Permissions. Features requiring a declined permission may be unavailable; activities that do not use it do not require you to grant it. The other three apps currently provide no camera or microphone features.']
    ]),
    ('platforms', ['6. Google Play, 외부 서비스와 제공 여부', '6. Google Play and external services'], [
        ['앱에는 제3자 광고 SDK, 행동 분석 SDK나 사용자 추적 목적의 원격 서비스를 넣지 않습니다. CrayonSmile은 위의 앱 로컬 데이터를 판매하거나 제3자에게 전송하지 않습니다.',
         'The apps contain no third-party advertising SDK, behavioral analytics SDK or remote user-tracking service. CrayonSmile does not sell or transmit the app-local data described above to third parties.'],
        ['유료 콘텐츠를 제공하는 앱의 구매·구매 복원과 추가 콘텐츠 배포는 Google Play 결제 및 배포 기능을 사용합니다. 앱은 콘텐츠 이용 권한을 확인하기 위해 상품 식별자, 구매·복원 상태와 필요한 구매 확인 정보를 처리할 수 있습니다. 결제 카드 번호나 Google 계정 비밀번호를 CrayonSmile이 직접 수집·저장하지 않습니다.',
         'Apps offering paid content use Google Play billing and delivery for purchases, restoration and additional content. An app may process product identifiers, purchase or restoration status and necessary purchase-verification information to check content entitlements. CrayonSmile does not directly collect or store payment card numbers or Google account passwords.'],
        ['Google은 설치·업데이트·결제·콘텐츠 다운로드·플랫폼 진단 과정에서 자체 정책에 따라 정보를 처리할 수 있습니다. 외부 링크로 이동한 뒤의 정보 처리는 해당 서비스 정책에 따릅니다. <a href="https://policies.google.com/privacy">Google 개인정보처리방침</a>을 참고해 주세요.',
         'Google may process information for installation, updates, billing, content downloads and platform diagnostics under its own policies. Information processed after following an external link is governed by that service. See the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.']
    ]),
    ('deletion', ['7. 보관·삭제와 안전한 관리', '7. Retention, deletion and safeguards'], [
        ['앱의 학습·설정·프로필·녹음 등 저장 데이터는 해당 기기에서 기능을 제공하는 동안 보관합니다. 앱 안에 제공된 개별 삭제·초기화 기능을 이용하거나, Android 설정에서 앱의 저장 데이터 지우기 또는 앱 삭제로 앱 내부 데이터를 삭제할 수 있습니다. 삭제한 로컬 진도와 녹음은 CrayonSmile 서버에서 복구할 수 없습니다.',
         'Saved learning records, settings, profiles and recordings remain on the device while they are used to provide app features. Use available in-app deletion or reset controls, Android’s clear-app-storage option, or uninstall the app to remove internal app data. CrayonSmile cannot restore deleted local progress or recordings from a server.'],
        ['갤러리에 따로 저장한 사진은 앞서 안내한 방법으로 별도 삭제해야 합니다. 앱을 지워도 Google Play의 구매 이력은 삭제되지 않으며, 구매 복원은 Google Play 계정과 제공 기능에 따릅니다.',
         'Separately saved gallery photos must be deleted separately as described above. Uninstalling an app does not delete Google Play purchase history; purchase restoration depends on the Google Play account and supported features.'],
        ['앱 내부 저장 공간과 Android 권한 체계를 이용하고, 사진 선택은 선택한 항목에 한정합니다. 앱에 원격 사용자 계정·프로필 데이터베이스나 앱 자체 클라우드 동기화를 운영하지 않습니다. 보호자는 기기 잠금과 접근 권한을 관리해 주세요.',
         'The apps use internal app storage and Android permissions, and photo selection is limited to the selected item. There is no remote app-user profile database or app-operated cloud sync. Guardians should manage device locks and access.']
    ]),
    ('children', ['8. 어린이와 보호자', '8. Children and guardians'], [
        ['앱은 어린이와 가족을 위한 로컬 놀이·학습을 제공합니다. 아동의 연락처·위치·광고 식별자를 운영자 서버로 수집하거나 광고 프로필을 만들지 않습니다. 가나다 한글놀이의 이름·나이는 기기 내 학습 프로필에 사용하며 온라인 회원가입 정보로 전송하지 않습니다.',
         'The apps provide local play and learning for children and families. They do not collect children’s contact details, location or advertising identifiers on an operator server or build advertising profiles. Names and ages in Hangul ABC are used in local learning profiles and are not transmitted as online account information.'],
        ['구매와 가족 내레이션 관리는 보호자 영역에서 제공합니다. 보호자가 프로필 입력, 권한 허용과 기기에 남기는 사진·녹음을 관리해 주세요. 개인정보에 관한 요청이나 우려는 아래 문의처로 알려주시면 확인하고 안내하겠습니다.',
         'Purchases and family narration management are provided in guardian areas. A guardian should manage profile entries, permissions and photos or recordings left on the device. Please contact us below with privacy requests or concerns so we can investigate and assist.']
    ]),
    ('support', ['9. 보호자가 이메일로 문의하는 경우', '9. When a guardian contacts support'], [
        ['보호자가 문의 이메일을 보내면 발신 주소, 문의 내용과 자발적으로 첨부한 자료를 답변·문제 해결을 위해 처리합니다. 이는 앱이 로컬 데이터를 자동 전송하는 기능과 별개입니다. 문의에 필요하지 않은 아동의 실명, 사진이나 녹음은 보내지 말아 주세요.',
         'If a guardian sends a support email, we process the sender address, message and voluntarily supplied attachments to respond and resolve the issue. This is separate from the apps, which do not automatically send their local data. Please do not send children’s real names, photos or recordings unless necessary for the enquiry.'],
        ['문의 자료는 답변과 후속 확인에 필요한 동안 보관하고, 더 이상 필요하지 않으면 삭제합니다. 법적 의무 이행이나 분쟁 대응을 위해 보존이 필요한 경우에는 그 목적과 필요한 기간에 한정합니다. 이메일 처리에는 Google의 이메일 서비스가 사용됩니다. 문의 자료의 열람·정정·삭제 요청도 같은 연락처로 보낼 수 있습니다.',
         'Support material is retained while needed for the reply and follow-up, then deleted when no longer required. Where retention is needed for a legal obligation or a dispute, it is limited to that purpose and necessary duration. Google’s email service is used for support correspondence. Requests to access, correct or delete support material can be sent to the same contact.']
    ]),
    ('website', ['10. 공식 웹사이트 방문', '10. Visiting this website'], [
        ['이 웹사이트는 GitHub Pages로 제공됩니다. GitHub는 서비스 제공과 보안을 위해 방문자의 IP 주소 등 접속 정보를 처리할 수 있습니다. 웹사이트는 Google Fonts에서 글꼴을 불러오므로 글꼴 요청이 Google 서버로 전송될 수 있습니다. 앱의 오프라인 로컬 처리와 웹사이트 방문 시의 통신은 서로 다릅니다.',
         'This website is hosted on GitHub Pages. GitHub may process connection information such as visitor IP addresses for service delivery and security. The website loads fonts from Google Fonts, so font requests may be sent to Google servers. These website connections are separate from offline processing inside the apps.'],
        ['CrayonSmile은 이 웹사이트에 광고·방문자 행동 분석 스크립트나 추적 픽셀을 추가하지 않았습니다. 호스팅·글꼴·외부 링크 제공자의 처리는 각 정책에 따릅니다. <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub 개인정보처리방침</a>과 <a href="https://policies.google.com/privacy">Google 개인정보처리방침</a>을 확인할 수 있습니다.',
         'CrayonSmile has not added advertising, visitor behavioral analytics scripts or tracking pixels to this website. Hosting, font and external-link providers process information under their own policies. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a> and <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.']
    ]),
    ('contact', ['11. 개인정보 문의처', '11. Privacy contact'], [
        ['운영자·개인정보 문의 담당: <strong>CrayonSmile</strong><br>이메일: <a href="mailto:crayonsmile.games@gmail.com">crayonsmile.games@gmail.com</a><br>기기 안에만 있는 진도·사진·녹음은 운영자가 원격으로 열람·수정·삭제할 수 없으므로, 필요한 기기 내 관리 방법을 안내해 드립니다.',
         'Operator and privacy contact: <strong>CrayonSmile</strong><br>Email: <a href="mailto:crayonsmile.games@gmail.com">crayonsmile.games@gmail.com</a><br>We cannot remotely view, change or delete progress, photos or recordings that exist only on your device. We can explain how to manage them on the device.']
    ]),
    ('changes', ['12. 변경 안내', '12. Changes to this policy'], [
        ['이 방침의 시행일은 <strong>2026년 10월 28일</strong>입니다. 이전 방침의 시행일은 2026년 6월 23일이며, 이번 개정은 네 앱의 적용 범위, 로컬 프로필, 카메라·사진과 권한, 삭제 방법, 이메일 문의 및 웹사이트 처리 내용을 구체화했습니다. 처리 목적·항목·제공 방식에 중요한 변경이 있으면 이 페이지와 필요한 앱 내 안내를 갱신합니다.',
         'This policy is effective <strong>October 28, 2026</strong>. The previous policy was effective June 23, 2026. This revision clarifies coverage of the four apps, local profiles, camera and photo access, permissions, deletion, support email and website data practices. Material changes to purposes, data types or sharing will be reflected on this page and in app notices where needed.']
    ])
]
