-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

use Baemin;

CREATE TABLE `User` (
    `userIdx` int AUTO_INCREMENT NOT NULL ,
    `name` varchar(30)  NOT NULL ,
    `email` varchar(50)  NOT NULL ,
    `profileImgUrl` text  NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (
        `userIdx`
    )
);

CREATE TABLE `Address` (
    `addressIdx` int AUTO_INCREMENT NOT NULL ,
    `userIdx` varchar(30)  NOT NULL ,
    `userAddress` varchar(50)  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'etc',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (
        `addressIdx`
    )
);

CREATE TABLE `Shop` (
    `shopIdx` int AUTO_INCREMENT NOT NULL ,
    `userIdx` int  NOT NULL ,
    `menuIdx` int  NOT NULL ,
    `menuNum` int  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (
        `shopIdx`
    )
);

CREATE TABLE `Food` (
    `foodIdx` int AUTO_INCREMENT NOT NULL ,
    `name` varchar(30)  NOT NULL ,
    `foodImgUrl` text  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (
        `foodIdx`
    )
);

CREATE TABLE `Store` (
    `storeIdx` int AUTO_INCREMENT NOT NULL ,
    `foodIdx` int  NOT NULL ,
    `name` varchar(30)  NOT NULL ,
    `storeImgUrl` text  NOT NULL ,
    `storeInfoMsg` text  NULL ,
    `availableWay` varchar(20)  NOT NULL ,
    `storeStar` float  NOT NULL ,
    `starNum` int  NOT NULL ,
    `reviewNum` int  NOT NULL ,
    `deliveryTimeMsg` varchar(30)  NOT NULL ,
    `leastPriceMsg` varchar(30)  NOT NULL ,
    `deliveryTipMsg` varchar(30)  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (
        `storeIdx`
    )
);

CREATE TABLE `Menu` (
    `menuIdx` int AUTO_INCREMENT NOT NULL ,
    `storeIdx` int  NOT NULL ,
    `name` varchar(50)  NOT NULL ,
    `menuImgUrl` text  NULL ,
    `menuInfoMsg` varchar(200)  NOT NULL ,
    `menuPrice` int  NOT NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (
        `menuIdx`
    )
);

CREATE TABLE `Review` (
    `reviewIdx` int AUTO_INCREMENT NOT NULL ,
    `userIdx` int  NOT NULL ,
    `storeIdx` int  NOT NULL ,
    `reviewImgUrl` text  NOT NULL ,
    `reviewStar` int  NOT NULL ,
    `reviewMsg` varchar(1000)  NOT NULL ,
    `ownerComment` text  NULL ,
    `status` varchar(10)  NOT NULL DEFAULT 'active',
    `createAt` timestamp  NOT NULL DEFAULT current_timestamp,
    `updateAt` timestamp  NOT NULL DEFAULT current_timestamp,
    PRIMARY KEY (
        `reviewIdx`
    )
);

CREATE TABLE `LikeStore` (
    `likeStoreIdx` int AUTO_INCREMENT NOT NULL ,
    `userIdx` int  NOT NULL ,
    `storeIdx` int  NOT NULL ,
    PRIMARY KEY (
        `likeStoreIdx`
    )
);

ALTER TABLE `Address` ADD CONSTRAINT `fk_Address_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Shop` ADD CONSTRAINT `fk_Shop_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Shop` ADD CONSTRAINT `fk_Shop_menuIdx` FOREIGN KEY(`menuIdx`)
REFERENCES `Menu` (`menuIdx`);

ALTER TABLE `Store` ADD CONSTRAINT `fk_Store_foodIdx` FOREIGN KEY(`foodIdx`)
REFERENCES `Food` (`foodIdx`);

ALTER TABLE `Menu` ADD CONSTRAINT `fk_Menu_storeIdx` FOREIGN KEY(`storeIdx`)
REFERENCES `Store` (`storeIdx`);

ALTER TABLE `Review` ADD CONSTRAINT `fk_Review_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `Review` ADD CONSTRAINT `fk_Review_storeIdx` FOREIGN KEY(`storeIdx`)
REFERENCES `Store` (`storeIdx`);

ALTER TABLE `LikeStore` ADD CONSTRAINT `fk_LikeStore_userIdx` FOREIGN KEY(`userIdx`)
REFERENCES `User` (`userIdx`);

ALTER TABLE `LikeStore` ADD CONSTRAINT `fk_LikeStore_storeIdx` FOREIGN KEY(`storeIdx`)
REFERENCES `Store` (`storeIdx`);

#--

DROP TABLE Shop;

INSERT into Food(name, foodImgUrl)
values
("1인분","www.1.url"),
("한식","www.hansik.url"),
("분식","www.bunsik.url"),
("카페.디저트","www.cafe.url"),
("돈까스.회.일식","www.j-food.url"),
("치킨","www.chicken.url"),
("피자","www.pizza.url");

ALTER TABLE Address MODIFY userIdx int ;

INSERT into Store(foodIdx, name, storeImgUrl, storeInfoMsg, availableWay, storeStar, starNum, reviewNum, deliveryTimeMsg, leastPriceMsg, deliveryTipMsg)
values
(1,"혼밥대왕","www.img.url2","안녕하세요 혼밥대왕 입니다","쿠폰",4.8,"100+",2882,"40~55분","6,900원","0~2,000원"),
(1,"김밥천국 건대점","www.img.url3","5차 재난지원금 사용가능합니다","쿠폰,포장",4.9,"100+",2419,"30~45분","6,500원","500~3,500원"),
(1,"배달삼겹 돼지되지 구의점","www.img.url4",">>>배달삼겹돼지되지 구의점입니다.","쿠폰,포장",4.9,"100+",3186,"39~54분","14,000원","0~2000원"),
(1,"열정국밥","www.img.url5","재료비 상승으로 인해 부득이하게 일부메뉴(순대국밥)가격을 조정","포장,매장",5.0,"100+",3679,"41~56분","8,000원","500~3,500원");

INSERT into Menu(storeIdx, name, menuImgUrl, menuInfoMsg, menuPrice)
values
(2,"프리미엄 족발 소","www.img1_1.url","국내산족발 소+막국수+매일담근보쌈김치+보쌈무겉절이+부추겉절이+각종야채세트",28000),
(2,"프리미엄 족발+생과일막국수","www.img1_2.url","귀한족발+귀한막국수+매일직접담근보쌈김치+보쌈무겉절이+부추겉절이+각종야채세트",34000),
(2,"환상의 조합 반반족발+생과일막국수","www.img1_3.url","귀한족발+직화족발+귀한막국수+매일직접담근보쌈김치+보쌈무겉절이+부추겉절이+각종야채세트",39000),
(2,"오늘 삶은 귀한보쌈+생과일막국수","www.img1_4.url","귀한족발+귀한막국수+매일직접담근보쌈김치+보쌈무겉절이+부추겉절이+각종야채세트",25000);

INSERT into Menu(storeIdx, name, menuImgUrl, menuPrice)
values
(3,"제주흑돼지김치찌개","www.img2_1.url",7400),
(3,"우삼겹된장찌개","www.img2_2.url",7900),
(3,"제주흑돼지볶음도시락","www.img2_3.url",8900),
(3,"돼지불백도시락","www.img2_4.url",8900);

INSERT into Menu(storeIdx, name, menuImgUrl, menuInfoMsg, menuPrice)
values
(4,"묵은지참치김밥(인기최고)","www.img2_1.url","건대점 김밥천국 시그니처 묵참김 김밥:)!",5000),
(4,"우삼겹된장찌개","www.img2_2.url","[[Upgrade:D]]보라색반죽은 자색고구마반죽이에요S2",7500),
(4,"제주흑돼지볶음도시락","www.img2_3.url","Best! 비빔국수계의 끝판왕",7500),
(4,"돼지불백도시락","www.img2_4.url","김밥김이 아닌 유부로 말았습니다!:D",5500);

INSERT into Menu(storeIdx, name, menuImgUrl, menuInfoMsg, menuPrice)
values
(5,"오리지날","www.img4_1.url","불판삼겹구이+쌈+공기밥+김치찌개+5가지반찬+카레가루+음료",15400),
(5,"양념","www.img4_2.url","불판삼겹구이+쌈+공기밥+김치찌개+5가지반찬+카레가루+음료",15900),
(5,"반반","www.img4_3.url","불판삼겹구이+쌈+공기밥+김치찌개+5가지반찬+카레가루+음료",21900),
(5,"파삼겹","www.img4_4.url","고기+5가지반찬+김치찌개+공기밥+상추+카레가루+콜라",16400);

INSERT into Menu(storeIdx, name, menuImgUrl, menuInfoMsg, menuPrice)
values
(6,"(야들야들~)돼지국밥","www.img5_1.url","열정국밥만의 특별한 기술로 고기를 1mm~2mm로 수작업하였습니다.",8000),
(6,"(시골순대국)토종순대국밥","www.img5_2.url","머릿고기+토종순대+돈사골육수+후추+파+부추+들깨가루",8500),
(6,"(깔끔단백~)살코기국밥","www.img5_3.url","살코기+후추+파+부추",8500);

INSERT INTO User(name, email, profileImgUrl)
values
("sangmin","sangmin@gmail.com","www.profileUrl1.url"),
("shyw****","shywii@gmail.com","www.profileUrl2.url"),
("sun","sunny@gmail.com","www.profileUrl3.url"),
("코코야 사랑해","lovecoco@gmail.com","www.profileUrl4.url");

INSERT INTO  Review(userIdx, storeIdx, reviewImgUrl, reviewStar, reviewMsg)
values
(4,2,"www.reviewImg3.url",5.0,"맛있어요~!~!~!~!~! 보쌈김치가 진짜 맛있어요ㅎㅎㅎ");

INSERT INTO LikeStore(userIdx, storeIdx)
values
(2,2),
(3,2),
(4,2);

INSERT INTO Shop(userIdx, menuIdx, menuNum)
values
(1,2,3),
(1,2,1);

INSERT INTO Address(userIdx, userAddress, status)
values
(1,"서울특별시 광진구 화양동 11-1","회사");

ALTER TABLE User ADD mailFlag int not null;
ALTER TABLE User ADD smsFlag int not null;
# --

# 1. 음식 종류
SELECT *
FROM Food;

# 2. 한식 식당 화면
# 1) 간추린 메뉴 등장 화면
SELECT storeIdx, GROUP_CONCAT(name) as shortMenuMsg
FROM Menu
GROUP BY storeIdx ;
# 2) 한식 식당 화면
SELECT S.storeImgUrl as "식당 사진", S.name as "식당 이름", S.availableWay as "가능한 주문 방법", S.storeStar as "식당 별점", S.starNum as "식당 평가수",
       shortMenu.shortMenuMsg as "간추린 메뉴" ,S.leastPriceMsg as "최소주문금액" ,substr(S.deliveryTipMsg,1,instr(S.deliveryTipMsg,'~')) as "배달 팁" , S.deliveryTimeMsg as "배달시간"
FROM Store S
INNER JOIN (SELECT storeIdx, GROUP_CONCAT(name) as shortMenuMsg
            FROM Menu
            GROUP BY storeIdx) shortMenu
ON S.storeIdx = shortMenu.storeIdx;

# 3. 음식점 메뉴
SELECT S.name as "식당 이름", M.name as "메뉴 이름", M.menuImgUrl as "메뉴 사진", ifnull(M.menuInfoMsg , '') as "메뉴 설명", M.menuPrice as "메뉴 가격"
FROM Store S
INNER JOIN Menu M on S.storeIdx = M.storeIdx
WHERE S.name = "귀한족발 건대직영점";

# 4. 리뷰 화면
SELECT S.name as "식당 이름",U.name as "유저 ID", reviewStar as "별점", reviewImgUrl as "리뷰 이미지", reviewMsg as "리뷰 글"
FROM Review R
INNER JOIN User U ON R.userIdx = U.userIdx
INNER JOIN Store S on R.storeIdx = S.storeIdx;

# 5. 찜 화면
SELECT U.name as "사용자 이름", S.name as "식당 이름",S.availableWay as "가능한 주문 방법", S.storeImgUrl as "식당 사진"
    ,S.storeStar as "식당 별점",S.starNum as "식당 평가수", shortMenu.shortMenuMsg as "간추린 메뉴", S.leastPriceMsg as "최소주문금액"
    ,substr(S.deliveryTipMsg,1,instr(S.deliveryTipMsg,'~')) as "배달 팁" , S.deliveryTimeMsg as "배달시간"
FROM LikeStore L
INNER JOIN User U on L.userIdx = U.userIdx
INNER JOIN Store S on L.storeIdx = S.storeIdx
INNER JOIN (SELECT storeIdx, GROUP_CONCAT(name) as shortMenuMsg
            FROM Menu
            GROUP BY storeIdx) shortMenu
ON L.storeIdx = shortMenu.storeIdx
WHERE U.userIdx = 1;

# 장바구니
SELECT St.name as StoreName, M.name as Menu, M.menuPrice as Price, Sh.menuNum as HowMany
FROM Shop Sh
INNER JOIN User U
INNER JOIN Menu M
INNER JOIN Store St
    on Sh.userIdx = U.userIdx
    and Sh.menuIdx = M.menuIdx
    and M.storeIdx = St.storeIdx
WHERE Sh.userIdx = 1;

# 7. 내 정보 화면
SELECT name as "닉네임", email as "이메일", User.userPhoneNum as "휴대폰 번호", User.mailFlag as "메일 수신 동의", User.smsFlag as "SMS 수신 동의"
FROM User
WHERE userIdx = 1;

# 8. 메뉴 상세 화면
SELECT menuImgUrl as "메뉴 사진", Menu.name as "메뉴 이름", menuInfoMsg as "메뉴 설명", menuPrice as "메뉴 가격", S.leastPriceMsg as "배달최소주문금액"
FROM Menu
INNER JOIN Store S
    on Menu.storeIdx = S.storeIdx
where menuIdx = 1;

# 9. 주소 설정 화면
SELECT userAddress as "주소", status as "장소"
FROM Address
WHERE userIdx = 1
ORDER BY addressIdx desc ;

















