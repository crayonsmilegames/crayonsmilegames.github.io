"""App-specific terms; shared clauses have one bilingual source.

Owner confirmed on 2026-11-05: public brand/email; free installation,
no ads/subscriptions, paid content only as guardian-facing one-time purchases.
Current Coloring release is free without IAP; Hangul billing is planned.
References reviewed: Google Play trader declaration (17594752), refund policy
(15574908), and Korea's Act on Consumer Protection in Electronic Commerce.
These pages do not replace seller disclosures in the store/checkout.
"""
EFFECTIVE = '2026-11-05'
VERSION = '1.0'
PACKAGES = {
    'somi-kids-world': 'com.crayonsmile.somikidsworld',
    'somi-coloring': 'com.crayonsmile.somicoloring',
    'hangul-abc': 'com.crayonsmile.somiganada',
    'somi-flashcards': 'com.crayonsmile.somiflashcards',
}

# Each item contains Korean and English reviewed copy, with HTML only for links.
APP = {
    'somi-kids-world': {
        'service': [
            ['한글·영어 놀이, 동화책 읽기와 듣기, 색칠·퍼즐 등 어린이와 가족을 위한 놀이 콘텐츠를 제공합니다. 이용 가능한 활동과 동화책은 설치한 버전 및 구매한 콘텐츠에 따라 달라집니다.',
             'The app offers Korean and English activities, storybook reading and listening, coloring, puzzles and other play for children and families. Available activities and books depend on the installed version and purchased content.'],
            ['보호자·가족 내레이션은 보호자가 자신의 목소리로 시작 인사와 동화책을 녹음하는 기능입니다. 녹음 기능이 포함된 유료 콘텐츠에서는 해당 기능을 콘텐츠 이용권의 일부로 제공하며 녹음 권한만 따로 판매하지 않습니다.',
             'Guardian and family narration lets a guardian record their own voice for greetings and storybooks. Where included in paid content, recording is part of that content entitlement, not a separately sold recording permission.'],
        ],
        'price': ['기본 설치와 무료 콘텐츠는 무료입니다. 일부 동화책·활동·콘텐츠 묶음은 보호자 영역에서 별도 일회성 구매로 제공합니다. 구매 화면에 명시된 콘텐츠만 포함되며, 별도 명시가 없으면 향후 출시되는 모든 콘텐츠까지 포함하지는 않습니다.',
                  'Installation and free content are free. Some storybooks, activities and content bundles are offered as separate one-time purchases in the guardian area. A purchase includes the content identified on its purchase screen, not all future releases unless expressly stated.'],
        'specific': [
            ['가족 녹음은 아동 음성 수집이나 음성 복제 서비스가 아닙니다. 보호자는 녹음할 권한이 있는 목소리만 녹음하고, 다른 성인의 목소리를 녹음할 때는 당사자의 허락을 받아 주세요. 녹음은 기기 내에 저장되며 앱이 업로드·원격 분석하지 않습니다. 보호자 녹음 관리에서 삭제할 수 있습니다.',
             'Family recording is not a service for collecting children’s voices or cloning voices. Guardians should record only voices they have permission to record and obtain another adult’s permission before recording that person. Recordings stay on the device, are not uploaded or remotely analyzed by the app, and can be deleted in guardian recording management.'],
            ['카메라 놀이는 선택적으로 사용합니다. 권한을 거부하거나 취소하면 해당 기능만 제한될 수 있습니다. 카메라 화면과 효과용 얼굴 위치 처리는 기기에서 이루어지며, 갤러리에 따로 저장한 사진은 앱 삭제 후에도 남을 수 있으므로 갤러리에서 별도로 삭제해 주세요.',
             'Camera play is optional. Declining or revoking permission may limit that feature. Camera frames and face positions used for effects are processed on the device. Photos separately saved to the gallery may remain after uninstalling and should be deleted separately in the gallery.'],
        ],
    },
    'somi-coloring': {
        'service': [
            ['한글 자음, 동물, 가족과 일상 도안에 색상과 브러시를 선택해 칠하는 색칠 놀이를 제공합니다. 소미 키즈월드 안의 색칠 활동과 별도로 설치·이용하는 앱입니다.',
             'The app offers coloring of Korean consonants, animals, family and everyday templates with selectable colors and brushes. It is installed and used separately from the coloring activity inside Somi Kids World.'],
        ],
        'price': ['현재 제공되는 소미 색칠놀이는 무료이며 인앱 결제와 광고가 없습니다. 향후 선택형 유료 콘텐츠를 도입하는 경우 보호자 영역의 일회성 구매로만 제공하고, 도입 전에 약관과 상품 안내를 갱신합니다. 기존 구매 없이 자동 결제되거나 구독으로 전환되지 않습니다.',
                  'The current Somi Coloring release is free and has no in-app purchases or ads. If optional paid content is introduced, it will be offered only as one-time purchases in the guardian area, with updated terms and product information before introduction. No automatic charge or subscription conversion will occur.'],
        'specific': [
            ['색칠 화면과 도구 설정은 기기에서 처리합니다. 카메라 촬영, 가족 음성 녹음, 작품의 온라인 게시·공유나 운영자 클라우드 보관 기능은 제공하지 않습니다. 저장·다시 열기 가능 여부는 앱에 실제 제공되는 기능을 기준으로 하며, 모든 작업 화면이 자동으로 보관되는 것은 아닙니다.',
             'The coloring canvas and tool settings are processed on the device. The app does not provide camera capture, family voice recording, online posting or sharing of artwork, or operator cloud storage. Saving and reopening depend on the features actually available in the app; not every working canvas is automatically retained.'],
        ],
    },
    'hangul-abc': {
        'service': [
            ['내 이름 글자 놀이, 한글 소리 듣기·따라 쓰기·글자 조립, 낱말 활동과 그림 이야기, 프로필별 학습·복습 기록을 제공합니다. 현재 출시 준비 중이며 정식 출시일과 최종 제공 범위는 공식 소개 및 앱의 안내로 공지합니다.',
             'The app provides name-based letter play, Korean sound listening, tracing and syllable building, word activities, illustrated stories, and per-profile learning and review records. It is being prepared for launch; the release date and final scope will be announced on the official product page and in the app.'],
        ],
        'price': ['기본 설치와 일부 체험 콘텐츠는 무료로 제공하고, 추가 학습 콘텐츠는 보호자 영역의 일회성 전체 이용권으로 제공할 계획입니다. 현재 실제 결제와 구매 복원은 준비 중이며 가격과 확정 상품 범위는 판매 개시 전에 표시합니다. 전체 이용권이라는 명칭만으로 향후 모든 별도 상품이 포함되는 것은 아니며, 포함 범위는 구매 시 상품 설명에 따릅니다.',
                  'Installation and selected trial content are planned to be free, with additional learning content offered through a one-time full-access purchase in the guardian area. Billing and purchase restoration are still being prepared; the price and confirmed product scope will be displayed before sales begin. The name “full access” does not by itself include every future separate product; the purchase description defines what is included.'],
        'specific': [
            ['이름 또는 별명, 나이, 아바타와 학습 기록은 기기 내 프로필에 사용합니다. 실명 대신 별명을 사용할 수 있습니다. 이 프로필은 온라인 회원 계정이 아니며 다른 기기에 자동 동기화되지 않습니다. 현재 카메라와 마이크를 사용하는 기능은 없습니다.',
             'A name or nickname, age, avatar and learning records are used for local profiles. A nickname may be used instead of a real name. Profiles are not online user accounts and are not automatically synchronized to other devices. There are currently no camera or microphone features.'],
        ],
    },
    'somi-flashcards': {
        'service': [
            ['한글·영어 그림 낱말카드, 소리 듣기와 답 고르기, 언어별 학습 기록 및 카드·마을 성장 놀이를 제공합니다. 현재 출시 준비 중이며 정식 서비스는 출시 안내에 따라 시작합니다.',
             'The app offers Korean and English picture word cards, listening and answer selection, separate learning records by language, and card and village progression. It is being prepared for launch, with service beginning as announced at release.'],
        ],
        'price': ['출시 시 기본 설치와 동물 꾸러미 20장은 무료로 제공할 예정입니다. 기본 완성팩 9개 꾸러미 180장과 탐험 확장팩 10개 꾸러미 200장은 각각 한글·영어를 포함하는 별도 일회성 인앱 구매 상품으로 준비하고 있습니다. 향후 추가 상품은 포함하지 않으며, 최종 구성과 가격은 판매 전에 표시합니다.',
                  'At launch, installation and the 20-card animal collection are planned to be free. The base completion pack (9 collections, 180 cards) and exploration expansion (10 collections, 200 cards) are being prepared as separate one-time in-app purchases, each including Korean and English. Future additional products are not included; final contents and prices will be shown before sales.'],
        'specific': [
            ['카드, 경험치, 마을과 반짝임 효과는 앱 내 놀이 요소이며 현금·실물 상품·투자 자산이 아닙니다. 현금 환전이나 이용자 간 거래 기능은 제공하지 않습니다. 카드 기울임에는 기기의 중력 센서를 사용할 수 있으며 입력은 기기에서 처리합니다. 현재 카메라·마이크 기능은 없습니다.',
             'Cards, experience, the village and shimmering effects are in-app play elements, not cash, physical goods or investment assets. There is no cash redemption or user-to-user trading. Card tilt may use the device’s gravity sensor, processed on the device. There are currently no camera or microphone features.'],
        ],
    },
}

def sections(slug):
    app = APP[slug]
    return [
        ('scope', ['1. 적용 범위와 서비스 제공자', '1. Scope and service provider'], [
            ['이 약관은 크레용스마일(CrayonSmile, 이하 “운영자”)이 제공하는 이 페이지에 명시된 앱의 이용 조건을 정합니다. 운영자는 대한민국 개인사업자이며 서비스 문의처는 <a href="mailto:crayonsmile.games@gmail.com">crayonsmile.games@gmail.com</a>입니다. 다른 크레용스마일 앱에는 각 앱의 별도 약관이 적용됩니다.',
             'These terms govern the app identified on this page, provided by CrayonSmile (the “operator”), a Korean sole proprietorship. Contact: <a href="mailto:crayonsmile.games@gmail.com">crayonsmile.games@gmail.com</a>. Other CrayonSmile apps have their own terms.'],
            ['앱을 이용하거나 구매를 결정하는 보호자는 이용 전에 이 약관과 상품 안내를 확인해 주세요. 법령상 별도 동의가 필요한 사항은 해당 동의 절차를 따릅니다. 이 웹페이지를 열었다는 사실만으로 구매·유료 전환·개인정보 추가 처리에 동의한 것으로 취급하지 않습니다.',
             'Guardians should review these terms and product information before use or purchase. Matters requiring separate consent by law follow the relevant consent procedure. Opening this webpage does not constitute consent to a purchase, conversion to paid use, or additional personal-data processing.'],
        ]),
        ('guardian', ['2. 어린이 이용과 보호자', '2. Children and guardians'], [
            ['앱은 어린이와 가족을 위한 놀이·학습용입니다. 미성년자의 계약·구매에는 관계 법령에 따른 법정대리인의 동의가 필요합니다. 필요한 동의 없이 이루어진 계약은 관계 법령에 따라 미성년자 또는 법정대리인이 취소할 수 있습니다.',
             'The app is for children’s and families’ play and learning. A minor’s contract or purchase requires legal-representative consent as required by applicable law. A minor or their legal representative may cancel a contract made without required consent in accordance with that law.'],
            ['보호자는 아이의 이용 시간, 음량, 기기 접근과 결제 인증을 관리해 주세요. 보호자 확인 화면은 아이의 우발적인 조작을 줄이기 위한 장치이며 Google Play의 구매 인증이나 법정대리인 동의를 대신하지 않습니다. 학습 성과나 발달 결과를 보장하는 서비스는 아닙니다.',
             'Guardians should manage playtime, volume, device access and payment authentication. A parent gate reduces accidental child interaction but does not replace Google Play purchase authentication or legally required consent. The app does not guarantee learning or developmental outcomes.'],
        ]),
        ('service', ['3. 이 앱의 제공 범위', '3. What this app provides'], app['service'] + [
            ['온라인 회원가입·이용자 간 채팅·광고·행동 분석 기반 추적은 제공하지 않습니다. 설치된 콘텐츠의 기본 놀이는 오프라인으로 이용할 수 있습니다. 설치·업데이트 및 제공되는 경우 구매·구매 복원·추가 콘텐츠 다운로드에는 인터넷과 Google Play가 필요할 수 있고 통신 요금은 가입한 통신 요금제에 따릅니다.',
             'There is no online app account sign-up, user-to-user chat, advertising or behavioral tracking. Basic play with installed content works offline. Installation, updates and, where available, purchases, restoration and additional downloads may require internet access and Google Play. Network charges depend on your provider’s plan.'],
        ]),
        ('purchases', ['4. 무료 이용과 유료 콘텐츠', '4. Free use and paid content'], [app['price'],
            ['광고와 정기 구독은 제공하지 않습니다. 유료 상품을 제공하는 경우 Google Play 결제를 이용하며 상품 구성, 가격, 세금 등 결제 조건을 구매 확정 전에 표시합니다. 무료 이용만으로 요금이 발생하지 않습니다. 이 약관의 구매 관련 조항은 실제 유료 상품을 제공하는 경우에만 적용됩니다.',
             'There are no ads or recurring subscriptions. Where paid products are available, payment uses Google Play, with product contents, price, taxes and payment conditions displayed before purchase confirmation. Free use alone does not incur a charge. Purchase clauses apply only where paid products are actually offered.'],
            ['구매한 이용권은 해당 앱과 상품 범위에 적용됩니다. 다른 크레용스마일 앱으로 자동 이전되거나 모든 앱의 이용권이 되지 않습니다. 구매 복원을 제공하는 경우 구매 당시의 Google Play 계정으로 복원할 수 있으나, 학습 진도·작품·녹음 등 로컬 데이터를 함께 복원하는 것은 아닙니다. 복원에 문제가 있으면 문의처로 알려 주세요.',
             'An entitlement applies to its specific app and product. It does not automatically transfer to other CrayonSmile apps or unlock all apps. Where restoration is offered, use the Google Play account used for purchase. Restoration does not restore local progress, artwork or recordings. Contact support if restoration fails.'],
        ]),
        ('refunds', ['5. 청약철회·환불과 구매 문제', '5. Withdrawal, refunds and purchase issues'], [
            ['유료 상품의 청약철회·환불은 적용되는 소비자보호 법령과 Google Play 환불 정책에 따라 처리합니다. 한국 소비자에게 적용되는 법정 청약철회권, 미성년자의 취소권, 미제공·하자·표시 또는 계약 내용과 다른 콘텐츠에 대한 권리를 이 약관으로 제한하지 않습니다.',
             'Withdrawal and refunds for paid products are handled under applicable consumer law and Google Play’s refund policy. These terms do not restrict statutory withdrawal rights, minors’ cancellation rights, or remedies for non-delivery, defects or content that differs from its description or contract.'],
            ['디지털콘텐츠의 공급 개시 등을 이유로 청약철회를 제한할 수 있는 경우에도 법에서 요구하는 사전 고지·체험 제공·동의 등 요건이 충족된 범위에서만 제한합니다. 다운로드하거나 실행했다는 이유만으로 모든 환불이 불가능하다고 보지 않습니다.',
             'Any withdrawal restriction based on the start of digital-content supply applies only to the extent that legal requirements, including required prior disclosures, trial access or consent, are satisfied. Downloading or running content does not make every refund unavailable.'],
            ['Google Play의 <a href="https://support.google.com/googleplay/answer/15574897?hl=ko">환불 요청 안내</a>에서 신청하거나 운영자에게 문의할 수 있습니다. 한국 외 지역의 권리도 해당 지역의 강행 소비자보호 규정에 따릅니다. 문의 시 앱 이름, 상품명, 구매일, 문제 내용과 필요한 경우 주문번호를 알려 주세요. 카드 번호·비밀번호나 불필요한 아동의 사진·녹음은 보내지 마세요.',
             'Request a refund through <a href="https://support.google.com/googleplay/answer/15574897?hl=en">Google Play’s refund instructions</a> or contact the operator. Mandatory consumer rights in other regions also apply. Include the app, product, purchase date, issue and, if needed, order number. Do not send card numbers, passwords or unnecessary children’s photos or recordings.'],
            ['결제 후 상품이 열리지 않거나 중복 결제·오류가 있으면 확인 후 이용권 복구, 재공급 또는 법령에 따른 환불 등 필요한 조치를 안내합니다. 취소·환불된 상품의 이용 권한은 회수될 수 있습니다. 앱 삭제만으로 환불이 신청되지는 않습니다.',
             'For missing access after payment, duplicate charges or errors, we will investigate and arrange entitlement recovery, redelivery or a refund as required by law. Access to cancelled or refunded products may be revoked. Uninstalling alone does not request a refund.'],
        ]),
        ('app-specific', ['6. 앱별 기능과 이용 시 유의사항', '6. App-specific features and care'], app['specific']),
        ('data', ['7. 기기 내 데이터와 개인정보', '7. Local data and privacy'], [
            ['앱의 진도·설정·프로필·작품·녹음 중 실제 제공하는 기능의 저장 데이터는 기기에서 관리합니다. 운영자의 사용자 데이터 서버나 앱 자체 클라우드 동기화는 없습니다. 기기 변경, 앱 삭제·저장 데이터 초기화 또는 기기 고장으로 로컬 데이터가 사라질 수 있고 운영자가 서버에서 복구할 수 없습니다. 이 안내는 운영자에게 법률상 책임이 있는 손해를 면제하는 조항이 아닙니다.',
             'Saved progress, settings, profiles, artwork and recordings, where those features exist, are managed on the device. There is no operator user-data server or app-operated cloud synchronization. Device changes, uninstalling, clearing app storage or device failure may remove local data, which the operator cannot recover from a server. This notice does not waive legally imposed liability.'],
            ['권한, 로컬 처리, Google Play 및 문의 이메일의 정보 처리, 삭제 방법은 <a href="/privacy/">개인정보처리방침</a>에 설명되어 있습니다. 이 약관은 개인정보의 추가 수집·외부 전송 동의를 대신하지 않습니다.',
             'Permissions, local processing, Google Play and support-email processing, and deletion are explained in the <a href="/en/privacy/">Privacy Policy</a>. These terms do not substitute for consent to additional collection or off-device transfer.'],
        ]),
        ('rights', ['8. 콘텐츠와 이용자가 만든 결과물', '8. Content and user creations'], [
            ['앱의 프로그램, 그림, 캐릭터, 음악·음성, 동화와 문구의 권리는 운영자 또는 정당한 권리자에게 있습니다. 이용자는 적법하게 제공된 범위에서 개인·가족의 비상업적 놀이와 학습에 사용할 수 있습니다. 구매는 콘텐츠의 저작권을 양도하는 것이 아닙니다.',
             'Rights in the app’s software, artwork, characters, music, audio, stories and text belong to the operator or their respective rights holders. Users may use lawfully supplied content for personal and family non-commercial play and learning. Purchasing content does not transfer its copyright.'],
            ['이용자가 직접 만든 그림·녹음 등에서 이용자에게 발생하는 권리는 이용자에게 남습니다. 운영자는 로컬 결과물을 업로드받거나 광고·학습 데이터로 사용하기 위한 이용허락을 이 약관으로 요구하지 않습니다. 결과물에 포함된 앱 도안·음악 등 기존 콘텐츠의 권리는 원래 권리자에게 남으며 법률상 허용되는 이용은 제한하지 않습니다.',
             'Any rights users acquire in their own drawings or recordings remain theirs. These terms do not require a license for the operator to upload local creations or use them for advertising or training data. Rights in pre-existing app templates, music and other included content remain with their holders; legally permitted uses are not restricted.'],
        ]),
        ('conduct', ['9. 적정한 이용과 제한', '9. Proper use and restrictions'], [
            ['타인의 권리를 침해하는 복제·재판매·무단 배포, 결제·접근 보호 장치의 부정 우회, 서비스나 다른 사람의 기기에 손해를 주는 행위는 하지 말아 주세요. 법률상 허용되는 호환성 연구, 접근성 이용, 인용 등은 이 조항으로 금지하지 않습니다.',
             'Do not infringe others’ rights through copying, resale or unauthorized distribution, fraudulently bypass payment or access controls, or damage the service or others’ devices. This clause does not prohibit interoperability research, accessibility uses, quotation or other conduct permitted by law.'],
            ['위반에 대응할 때에는 필요한 범위에서 조치하고, 가능한 경우 사유·기간·이의 제기 방법을 안내합니다. 제한에 이의가 있으면 문의처로 확인을 요청할 수 있습니다. 유료 이용권의 제한에도 법령상 권리와 정당한 구제 절차를 보장합니다.',
             'Responses to violations will be proportionate, with reasons, duration and a way to raise objections where possible. Contact support to request a review of a restriction. Any restriction of paid access remains subject to statutory rights and appropriate remedies.'],
        ]),
        ('changes', ['10. 업데이트·서비스 변경과 종료', '10. Updates, service changes and discontinuation'], [
            ['기기·운영체제와의 호환성, 보안, 오류 개선이나 콘텐츠 운영을 위해 업데이트할 수 있습니다. 중요한 기능·이용 조건의 변경은 공식 웹사이트 또는 앱의 공지로 알립니다. 앱 업데이트나 다운로드는 기기 저장 공간과 지원되는 Google Play 환경을 필요로 할 수 있습니다.',
             'Updates may address device or operating-system compatibility, security, bugs or content operations. Material changes to features or use conditions will be announced on the official website or in the app. Updates and downloads may require device storage and a supported Google Play environment.'],
            ['서비스 종료나 이미 구매한 콘텐츠의 중대한 축소가 필요한 경우 원칙적으로 30일 전에 사유·시점·기존 구매자 조치와 문의 방법을 알립니다. 긴급한 보안·법적 사유로 사전 안내가 어려우면 가능한 한 신속히 안내합니다. 법령과 구매 조건에 따라 계속 이용 방법, 대체 제공 또는 환불 등 필요한 조치를 하며 임의 변경만으로 기존 구매자의 권리를 소멸시키지 않습니다.',
             'If discontinuation or a substantial reduction of purchased content is necessary, we will ordinarily give 30 days’ notice of the reason, timing, arrangements for existing purchasers and contact method. If urgent security or legal reasons prevent advance notice, we will notify users as soon as possible. Continued access, alternatives or refunds will be arranged as required by law and purchase conditions; unilateral changes do not extinguish existing purchasers’ rights.'],
        ]),
        ('liability', ['11. 책임과 소비자 권리', '11. Liability and consumer rights'], [
            ['운영자와 이용자는 각자의 귀책사유로 상대방에게 발생시킨 손해에 대해 관계 법령에 따라 책임을 집니다. 운영자는 고의·과실에 따른 책임, 유료 콘텐츠의 계약상 의무 및 법률상 배제할 수 없는 소비자 권리를 포괄적으로 면제하거나 제한하지 않습니다.',
             'The operator and users are responsible under applicable law for harm attributable to them. The operator does not broadly waive or restrict liability for intentional or negligent conduct, contractual obligations for paid content, or consumer rights that cannot legally be excluded.'],
            ['기기·통신 장애나 불가항력에 따른 문제는 실제 원인과 당사자의 귀책사유에 따라 판단합니다. 이 약관에 규정되지 않은 사항이나 약관 일부가 무효인 경우에는 적용 법령을 따르며 나머지 조항은 유효한 범위에서 적용합니다.',
             'Device, network and force-majeure issues are assessed according to their actual cause and attributable fault. Applicable law governs matters not covered here and any invalid clause; remaining clauses apply to the extent valid.'],
        ]),
        ('notice', ['12. 약관 변경·준거법과 문의', '12. Changes to terms, governing law and contact'], [
            ['약관을 바꿀 때에는 변경 내용·이유·시행일을 이 페이지 또는 앱 공지로 원칙적으로 시행 7일 전에 알리고, 이용자에게 불리하거나 중요한 변경은 30일 전에 안내합니다. 동의가 필요한 변경은 별도 동의를 받으며 침묵만으로 동의한 것으로 취급하지 않습니다. 이미 성립한 구매 계약의 권리는 관계 법령과 해당 계약에 따라 보호합니다.',
             'Changes to these terms will ordinarily be announced on this page or in the app at least 7 days before taking effect, with the changes, reasons and effective date. Material or adverse changes receive 30 days’ notice. Separate consent will be obtained where required; silence alone is not consent. Rights under existing purchase contracts remain protected by applicable law and those contracts.'],
            ['이 약관에는 대한민국 법률을 적용하되 이용자 거주 국가에서 배제할 수 없는 소비자보호 규정과 재판 관할권을 제한하지 않습니다. 분쟁은 먼저 문의처를 통해 해결을 시도하고, 해결되지 않으면 관계 법령에 따른 분쟁조정 절차 또는 관할 법원에서 처리할 수 있습니다. 한국어와 영어 문구의 차이가 법정 권리를 제한하지 않습니다.',
             'Korean law governs these terms without restricting non-excludable consumer protections or jurisdiction rights in the user’s country of residence. Please first contact support to seek resolution. Unresolved disputes may use statutory dispute-resolution procedures or a competent court. Differences between Korean and English wording do not limit statutory rights.'],
            ['서비스·구매·약관 문의: <a href="mailto:crayonsmile.games@gmail.com">crayonsmile.games@gmail.com</a>. 문의에는 앱 이름과 문제 해결에 필요한 최소한의 정보만 포함해 주세요.',
             'Service, purchase and terms enquiries: <a href="mailto:crayonsmile.games@gmail.com">crayonsmile.games@gmail.com</a>. Include the app name and only the information needed to resolve the issue.'],
        ]),
    ]
