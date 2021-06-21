SQL> alter table membert01
  2  add mem_notice varchar2(30);

Table altered.

SQL> select * from membert01;

MEM_NAME                                 MEM_ID                                   MEM_PWD
                                   MEM_EMAIL
---------------------------------------- ---------------------------------------- ---------------------------------------- ------------------------------------------------------------
MEM_PHONE                                MEM_ADDR
              MEM_NOTICE
---------------------------------------- ------------------------------------------------------------ ------------------------------------------------------------
오렌지                                   orange                                   1234
                                   orange@test.com
032                                      재능대학교

장미                                     red                                      1234
                                   red@test.com
044                                      홍익대학교

개나리                                   yellow                                   1234
                                   yellow@test.com
032                                      재능대학교

소나무                                   green                                    1234
                                   green@test.com
044                                      홍익대학교

바다                                     blue                                     1234
                                   blue@test.com
044                                      홍익대학교


SQL> desc membert01;
 Name
                           Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 MEM_NAME
                                    VARCHAR2(20)
 MEM_ID
                                    VARCHAR2(20)
 MEM_PWD
                                    VARCHAR2(20)
 MEM_EMAIL
                                    VARCHAR2(30)
 MEM_PHONE
                                    VARCHAR2(20)
 MEM_ADDR
                                    VARCHAR2(30)
 MEM_NOTICE
                                    VARCHAR2(30)

SQL> alter table membert01
  2  modify mem_notice varchar2(20);

Table altered.

SQL> desc membert01;
 Name
                           Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 MEM_NAME
                                    VARCHAR2(20)
 MEM_ID
                                    VARCHAR2(20)
 MEM_PWD
                                    VARCHAR2(20)
 MEM_EMAIL
                                    VARCHAR2(30)
 MEM_PHONE
                                    VARCHAR2(20)
 MEM_ADDR
                                    VARCHAR2(30)
 MEM_NOTICE
                                    VARCHAR2(20)

SQL> alter table membert01
  2  drop column mem_notice;

Table altered.

SQL> desc membert01;
 Name
                           Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 MEM_NAME
                                    VARCHAR2(20)
 MEM_ID
                                    VARCHAR2(20)
 MEM_PWD
                                    VARCHAR2(20)
 MEM_EMAIL
                                    VARCHAR2(30)
 MEM_PHONE
                                    VARCHAR2(20)
 MEM_ADDR
                                    VARCHAR2(30)






