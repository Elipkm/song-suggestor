
  CREATE TABLE "SONG_DATA" 
   (	
    "ID" NUMBER(19,0),
    "TITLE" VARCHAR2(300), 
	"ARTIST" VARCHAR2(300), 
	"LYRICS" VARCHAR2(4000) 
   );

  CREATE TABLE "SONG_KEYWORD" 
   (	
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT, 
	"SONG_ID" NUMBER, 
	"KEYWORD_ID" NUMBER, 
	"KEYWORD" VARCHAR2(300)
   );

