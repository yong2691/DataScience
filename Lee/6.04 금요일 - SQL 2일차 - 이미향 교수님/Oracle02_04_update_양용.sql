SQL> update membert01
  2  set mem_pwd='4321'
  3  where mem_id='orange';

1 row updated.

SQL> select * from membert01;

MEM_NAME                                 MEM_ID                                   MEM_PWD
                                   MEM_EMAIL
---------------------------------------- ---------------------------------------- ---------------------------------------- ------------------------------------------------------------
MEM_PHONE                                MEM_ADDR
---------------------------------------- ------------------------------------------------------------
오렌지                                   orange                                   4321
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


SQL>