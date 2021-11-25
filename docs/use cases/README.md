# Модель прецедентів

В даному файлі наведені графічні діаграми що відображують бізнес процеси.

Вбудовування зображень діаграм здійснюється з використанням сервісу [UML Editor](https://jace-dev.herokuapp.com/design/uml-editor#/), що створений Андрієм Болдаком.

В markdown-файлі використовується опис діаграми.

- Загальна діаграма бізнес процесів:

![General Diagram](https://user-images.githubusercontent.com/31734600/142782266-94a6df78-9d32-4a05-8be8-51d2fbb35888.png)
<br><br><br>
**Діаграми прецедентів**
<br><br>

- ID: v1.NOT_LOGGED.001

    <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

        left header
             <font color=000 size=10><b>ID:</b> v1.NOT_LOGGED.001
             <font color=000 size=10><b>НАЗВА:</b> Зареєструватись у системі
             <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
             <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
             <font color=000 size=10>Користувач не зареєстрований у системі.
             <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Новий обліковий запис
             <font color=000 size=10><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
             <font color=000 size=10>v1.NOT_LOGGED.EX.001
         end header

         |Користувач|
             start
             : Натискає кнопку "Реєстрація" ;
             : Передає реєстраційні данні:
             Логін, пароль та пошта;

         |Система|
             : Перевіряє переданні реєстраційні данні;

             note right #ff0000
             <b>Можлива</b>
             <b>v1.NOT_LOGGED.EX.001</b>
             end note

             : створює обліковий запис за переданими
             реєстраційними даними;

             : надає користувачу інформацію про
             створення облікового запису;

         |Користувач|
             stop;

  @enduml

    </center>

- ID: v1.NOT_LOGGED.002

  <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

      left header
           <font color=000 size=10><b>ID:</b> v1.NOT_LOGGED.002
           <font color=000 size=10><b>НАЗВА:</b> Авторизуватись у системі
           <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
           <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
           <font color=000 size=10>Користувач зареєстрований у системі.
           <font color=000 size=10>Користувач не авторизований у системі.
           <font color=000 size=10><b>РЕЗУЛЬТАТ:</b>Сеанс роботи
           <font color=000 size=10><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
           <font color=000 size=10>v1.NOT_LOGGED.EX.002
           <font color=000 size=10>v1.NOT_LOGGED.EX.003
       end header

       |Користувач|
           start
           : Натискає кнопку "Вхід" ;
           : Передає авторизаційні дані:
           Логін та пароль;

       |Система|
           : ідентифікує користувача;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.NOT_LOGGED.EX.002</b>
           end note

           : авторизує користувача, та
           надає користувачу авторизацію у системі;

         |Користувач|
             stop;

  @enduml

    </center>

- ID: v1.USER.001

  <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

      left header
           <font color=000 size=10><b>ID:</b> v1.USER.001
           <font color=000 size=10><b>НАЗВА:</b> 	Отримати дані для проходження опитування
           <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
           <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
           <font color=000 size=10>Користувач авторизований у системі.
           <font color=000 size=10>Користувач має доступ до запитаного опитування.
           <font color=000 size=10><b>РЕЗУЛЬТАТ:</b>Дані для проходження опитування
           <font color=000 size=10><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
           <font color=000 size=10>v1.NOT_LOGGED.EX.004
           <font color=000 size=10>v1.COMMON.EX.001
           <font color=000 size=10>v1.COMMON.EX.002
       end header

       |Користувач|
           start
           : Натискає кнопку "Пройти опитування" ;

       |Система|
           : ідентифікує користувача;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.NOT_LOGGED.EX.004</b>
           end note

           :знаходить дані для проходження опитування;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.COMMON.EX.001</b>
           end note

           :авторизує користувача для отримання даних;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.COMMON.EX.002</b>
           end note

           :надає користувачу дані для проходження опитування;

       |Користувач|

       :отримує дані для проходження опитування.;
           stop;

  @enduml

     </center>

- ID: v1.USER.002

    <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

        left header
             <font color=000 size=10><b>ID:</b> v1.USER.002
             <font color=000 size=10><b>НАЗВА:</b>Отримати дані для проходження опитування
             <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
             <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
             <font color=000 size=10>Користувач авторизований у системі.
             <font color=000 size=10>Користувач має доступ до запитаного опитування.
             <font color=000 size=10>Користувач коректно пройшов опитування.
             <font color=000 size=10><b>РЕЗУЛЬТАТ:</b>Повідомлення про зарахування результатів опитування користувача
             <font color=000 size=10><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
             <font color=000 size=10>v1.NOT_LOGGED.EX.004
             <font color=000 size=10>v1.COMMON.EX.001
             <font color=000 size=10>v1.COMMON.EX.002
             <font color=000 size=10>v1.COMMON.EX.003
         end header

         |Користувач|
             start
             : Натискає кнопку "Завершити опитування" ;

         |Система|
             : ідентифікує користувача;

             note right #ff0000
             <b>Можлива</b>
             <b>v1.NOT_LOGGED.EX.004</b>
             end note

             :перевіряє правильність даних про проходження опитування;

             note right #ff0000
             <b>Можлива</b>
             <b>v1.COMMON.EX.003</b>
             end note

             :надає користувачу повідомлення про зарахування результатів опитування;

         |Користувач|
             stop;

  @enduml

  </center>

- ID: v1.USER.003

    <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

      left header
           <font color=000 size=10><b>ID:</b> v1.USER.003
           <font color=000 size=10><b>НАЗВА:</b> Отримати зворотній зв'язок стосовно надісланого опитування
           <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
           <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
           <font color=000 size=10>Користувач авторизований у системі.
           <font color=000 size=10>Користувач має доступ до запитаного опитування.
           <font color=000 size=10>Користувач коректно пройшов опитування.
           <font color=000 size=10>У системі є дані про зворотній зв'язок стосовно опитування
           <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Зворотній зв'язок стосовно надісланого опитування
           <font color=000 size=10><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
           <font color=000 size=10>->v1.NOT_LOGGED.EX.004
           <font color=000 size=10>->v1.COMMON.EX.001
           <font color=000 size=10>->v1.COMMON.EX.002
           <font color=000 size=10>->v1.COMMON.EX.003
       end header
       |Користувач|
           start
           : Натискає на отримання
           даних про зворотній зв'язок
           стосовно опитування;
       |Система|
           : Шукає користувача у
           базі даних користувачів
           та ідентифікує його;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.NOT_LOGGED.EX.004</b>
           end note

           : Перевіряє, чи існує задане опитування;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.COMMON.EX.001</b>
           end note

           : Перевіряє, чи є доступ
           у користувача до заданого
           опитування;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.COMMON.EX.002</b>
           end note

           : Перевіряє правильність даних
           про проходження користувачем опитування;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.COMMON.EX.003</b>
           end note

           : Шукає дані про задане опитування;

           : Надає користувачу дані про зворотній
           зв'язок стосовно опитування;
       |Користувач|
           stop;

  @enduml

  </center>

- ID: v1.ORGANIZATION.001

    <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

      left header
           <font color=000 size=10><b>ID:</b> v1.ORGANIZATION.001
           <font color=000 size=10><b>НАЗВА:</b> Створити організацію
           <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
           <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>Користувач авторизований у системі.
           <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про створення організації
           <font color=000 size=10><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
           <font color=000 size=10>->v1.NOT_LOGGED.EX.004
           <font color=000 size=10>->v1.COMMON.EX.003
       end header

       |Користувач|
           start
           : Надсилає запит на
           створення організації ;

       |Система|
           : Шукає користувача у
           базі даних користувачів
           та ідентифікує його;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.NOT_LOGGED.EX.004</b>
           end note

           : Надає користувачу форму
           для заповнення даних
           про організацію;

       |Користувач|
           : Надає у формі потрібні
           дані про організацію;

       |Система|
           : Перевіряє правильність
           надісланих даних;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.COMMON.EX.003</b>
           end note

           : Створює організацію;

           : Надсилає користувачу дані
           про створення організації;
       |Користувач|
           stop;

  @enduml

  </center>

- ID: v1.ORGANIZATION.002

    <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

      left header
           <font color=000 size=10><b>ID:</b> v1.ORGANIZATION.002
           <font color=000 size=10><b>НАЗВА:</b> Отримати дані про організацію
           <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
           <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
           <font color=000 size=10>Користувач авторизований у системі.
           <font color=000 size=10>Користувач має доступ до запитаної організації.
           <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Дані про організацію
           <font color=000 size=10><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
           <font color=000 size=10>v1.NOT_LOGGED.EX.004
           <font color=000 size=10>v1.COMMON.EX.001
           <font color=000 size=10>v1.COMMON.EX.002
       end header

       |Користувач|
           start
           : Запитує дані
           про організацію ;

       |Система|
           : Ідентифікує користувача;
           note right #ff0000
           <b>Можлива</b>
           <b>v1.NOT_LOGGED.EX.004</b>
           end note

           : Перевіряє, чи
           існує організація;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.COMMON.EX.001</b>
           end note

           : Знаходить дані
           про організацію;

           : Авторизує користувача
           для отримання даних
           про організацію;

           note right #ff0000
           <b>Можлива</b>
           <b>v1.COMMON.EX.002</b>
           end note

           : Надсилає користувачу
           дані про організацію;
       |Користувач|
           stop;

  @enduml

  </center>

- ID: v1.ORGANIZATION.003

    <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

      left header
         <font color=000 size=10><b>ID:</b> v1.ORGANIZATION.003
         <font color=000 size=10><b>НАЗВА:</b> Змінити дані про організацію
         <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
         <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
         <font color=000 size=10>Користувач авторизований у системі.
         <font color=000 size=10>Користувач має доступ до запитаної організації.
         <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про зміну даних організації.
         <font color=000 size=10><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
         <font color=000 size=10>v1.NOT_LOGGED.EX.004
         <font color=000 size=10>v1.COMMON.EX.001
         <font color=000 size=10>v1.COMMON.EX.002
         <font color=000 size=10>v1.COMMON.EX.003

  end header

  |Користувач|
  start
  : Запитує зміну
  даних про організацію ;

  |Система|
  : Ідентифікує користувача;

         note right #ff0000
         <b>Можлива</b>
         <b>v1.NOT_LOGGED.EX.004</b>
         end note

         : Перевіряє, чи
         існує організація;

         note right #ff0000
         <b>Можлива</b>
         <b>v1.COMMON.EX.001</b>
         end note

         : Знаходить дані
         про організацію;

         : Авторизує користувача
         для зміни даних
         про організацію;

         note right #ff0000
         <b>Можлива</b>
         <b>v1.COMMON.EX.002</b>
         end note

         : Надає користувачу форму
         для заповнення змінених
         даних про організацію;

  |Користувач|
  : Заповнює форму
  зміненими даними;

  |Система|
  : Перевіряє правильність
  надісланих даних;

         note right #ff0000
         <b>Можлива</b>
         <b>v1.COMMON.EX.003</b>
         end note

         : Змінює дані
         про організацію;

         : Надсилає користувачу
         повідомлення про зміну
         даних організації;

  |Користувач|
  stop;

  @enduml

  </center>

- ID: v1.ORGANIZATION.004

  <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

      left header
        <font color=000 size=18><b>ID:</b> v1.ORGANIZATION.004
        <font color=000 size=16><b>НАЗВА:</b> Створити опитування
        <font color=000 size=16><b>УЧАСНИКИ:</b> Користувач, Система
        <font color=000 size=16><b>ПЕРЕДУМОВИ:</b>
        <font color=000 size=16>1.Користувач авторизований у системі.
        <font color=000 size=16>2.Користувач має доступ до запитаної організації.
        <font color=000 size=16><b>РЕЗУЛЬТАТ:</b> Повідомлення про створення опитування.
        <font color=000 size=16><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
        <font color=000 size=16>v1.NOT_LOGGED.EX.004
        <font color=000 size=16>v1.COMMON.EX.001
        <font color=000 size=16>v1.COMMON.EX.002
        <font color=000 size=16>v1.COMMON.EX.003
        <font color=000 size=16><b>ОСНОВНИЙ СЦЕНАРІЙ:</b>

  end header

  |Користувач|
  start
  :Користувач авторизується
  в системі;

        :Користувач відкриває
        форму запиту
        створення опитування;

        :Користувач заповнює форму
        запиту даними;

        :Користувач нажимає
        кнопку "Відправити запит";

  |Система|
  :Система ідентифікує
  користувача;
  note right #ffaaaa
  <b>Можлива</b>
  <b>v1.NOT_LOGGED.EX.004</b>
  end note

        :Система знаходить дані
        про організацію;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.COMMON.EX.001</b>
        end note

        :Система авторизує користувача
        для створення опитування;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.COMMON.EX.002</b>
        end note

        :Система перевіряє
        правильність надісланих даних;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.COMMON.EX.003</b>
        end note

        :Система створює опитування;

        :Система надсилає
        користувачу повідомлення про
        створення опитування;

  |Користувач|
  :Користувач отримує
  повідомлення від системи
  про створення опитування;

        :Користувач ознайомлюється
        з повідомлення;

        :Користувач закриває
        повідомлення від системи;

        :Користувач завершує
        взаємодію;

  stop;

  @enduml
         
  </center>

- ID: v1.ORGANIZATION.005

  <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

  left header
  <font color=000 size=18><b>ID:</b> v1.ORGANIZATION.005
  <font color=000 size=16><b>НАЗВА:</b> Змінити дані про опитування
  <font color=000 size=16><b>УЧАСНИКИ:</b> Користувач, Система
  <font color=000 size=16><b>ПЕРЕДУМОВИ:</b>
  <font color=000 size=16>1.Користувач авторизований у системі.
  <font color=000 size=16>2.Користувач має доступ до запитаної організації.
  <font color=000 size=16><b>РЕЗУЛЬТАТ:</b> Повідомлення про змінення даних опитування.
  <font color=000 size=16><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
  <font color=000 size=16>v1.NOT_LOGGED.EX.004
  <font color=000 size=16>v1.COMMON.EX.001
  <font color=000 size=16>v1.COMMON.EX.002
  <font color=000 size=16>v1.COMMON.EX.003
  <font color=000 size=16><b>ОСНОВНИЙ СЦЕНАРІЙ:</b>

  end header

  |Користувач|
  start
  :Користувач авторизується
  в системі;

        :Користувач відкриває
        форму запиту
        на змінення опитування;

        :Користувач заповнює форму
        запиту даними;

        :Користувач нажимає
        кнопку "Відправити запит";

  |Система|
  :Система отримує запит
  від користувача;

        :Система ідентифікує
        користувача;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.NOT_LOGGED.EX.004</b>
        end note

        :Система знаходить дані
        про організацію
        та опитування;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.COMMON.EX.001</b>
        end note

        :Система авторизує користувача
        для змінення опитування;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.COMMON.EX.002</b>
        end note

        :Система перевіряє
        правильність надісланих даних;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.COMMON.EX.003</b>
        end note

        :Система змінює опитування;

        :Система надсилає
        користувачу повідомлення про
        змінення опитування;

  |Користувач|
  :Користувач отримує
  повідомлення від системи
  про змінення опитування;

        :Користувач ознайомлюється
        з повідомлення;

        :Користувач закриває
        повідомлення від системи;

        :Користувач завершує
        взаємодію;

  stop;

  @enduml

  </center>

- ID: v1.ORGANIZATION.006

  <center style="border-radius:4px; border: 1px solid #cfd7e6; box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025); padding: 1em;">

  @startuml

  left header
  <font color=000 size=18><b>ID:</b> v1.ORGANIZATION.006
  <font color=000 size=16><b>НАЗВА:</b> Отримати результати опитування
  <font color=000 size=16><b>УЧАСНИКИ:</b> Користувач, Система
  <font color=000 size=16><b>ПЕРЕДУМОВИ:</b>
  <font color=000 size=16>1.Користувач авторизований у системі.
  <font color=000 size=16>2.Користувач має доступ до запитаної організації.
  <font color=000 size=16><b>РЕЗУЛЬТАТ:</b> Результати опитування
  <font color=000 size=16><b>ВИКЛЮЧНІ СИТУАЦІЇ:</b>
  <font color=000 size=16>v1.NOT_LOGGED.EX.004
  <font color=000 size=16>v1.COMMON.EX.001
  <font color=000 size=16>v1.COMMON.EX.002
  <font color=000 size=16><b>ОСНОВНИЙ СЦЕНАРІЙ:</b>

  end header

  |Користувач|
  start
  :Користувач авторизується
  в системі;

        :Користувач відкриває
        форму запиту
        результатів опитування;

        :Користувач нажимає
        кнопку "Відправити запит";

  |Система|
  :Система отримує запит
  від користувача;

        :Система ідентифікує
        користувача;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.NOT_LOGGED.EX.004</b>
        end note

        :Система перевіряє
        рівень доступу користувача;

        :Система знаходить дані
        про організацію
        та опитування;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.COMMON.EX.001</b>
        end note

        :Система авторизує
        користувача для отримання
        результатів опитування;
        note right #ffaaaa
        <b>Можлива</b>
        <b>v1.COMMON.EX.002</b>
        end note

        :Система надсилає
        користувачу результати
        опитування;

  |Користувач|
  :Користувач отримує
  повідомлення з результатами
  від системи;

        :Користувач ознайомлюється
        з повідомленням;

        :Користувач закриває
        повідомлення від системи;

        :Користувач завершує
        взаємодію;

  stop;

  @enduml

  </center>

- ID: v1.NOT_LOGGED.EX.004

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;" >
    
@startuml
  
    left header
         <font color=000 size=10><b>ID:</b> v1.NOT_LOGGED.EX.004
         <font color=000 size=10><b>НАЗВА:</b> Відхілити доступ для неавторизованого користувача
         <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система 
         <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
         <font color=000 size=10>Користувач не авторизований у системі.
         <font color=000 size=10>Система відхилила запит неавторизованого користувача.
         <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про відхиленя доступу для неавторизованого користувача.
     end header
     |Система|
         start
         : Надає користувачу повідомлення
         про відхиленя доступу 
         для неавторизованого користувача.;
     |Користувач|
         : Отримує повідомлення про 
         відхиленя доступу для 
         неавторизованого користувача.;
     |Система|
         : Завершує взаємодію;
         stop;
@enduml
</center>

- ID: v1.COMMON.EX.001

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;" >
    
@startuml
  
    left header
         <font color=000 size=10><b>ID:</b> v1.COMMON.EX.001
         <font color=000 size=10><b>НАЗВА:</b> Повідомити про відсутність запитаних даних
         <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система 
         <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
         <font color=000 size=10>Користувач авторизований у системі.
         <font color=000 size=10>Користувач запитав дані, що відсутні у системі.
         <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про відсутність запитаних даних.
     end header
     |Система|
         start
         : Надає користувачу повідомлення 
         про відсутність запитаних даних.;
     |Користувач|
         : Отримує повідомлення 
         про відсутність запитаних даних.;
     |Система|
         : Завершує взаємодію;
         stop;
@enduml
</center>

- ID: v1.COMMON.EX.002

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;" >
    
@startuml
  
    left header
         <font color=000 size=10><b>ID:</b> v1.COMMON.EX.002
         <font color=000 size=10><b>НАЗВА:</b> Відхилити доступ користувача до даних
         <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система 
         <font color=000 size=10><b>ПЕРЕДУМОВИ:</b> Система відхилила запит користувача до даних.
         <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про відхилення доступу до даних.
     end header
     |Система|
         start
         : Надає користувачу повідомлення 
         про відхилення доступу до даних.;
     |Користувач| 
         : Отримує повідомлення 
         про відхилення доступу до даних.;
     |Система|
         : Завершує взаємодію;
         stop;
@enduml
</center>

- ID: v1.COMMON.EX.003

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;" >

@startuml

    left header
         <font color=000 size=10><b>ID:</b> v1.COMMON.EX.003
         <font color=000 size=10><b>НАЗВА:</b> Відхилити хибні дані
         <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
         <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
         <font color=000 size=10>Користувач авторизований у системі.
         <font color=000 size=10>Користувач надіслав у систему хибні дані.
         <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про відхилення хибних даних.
     end header
     |Система|
         start
         : Надає користувачу повідомлення
         про відхилення хибних даних.;
     |Користувач|
         : Отримує повідомлення
         про відхилення хибних даних.;
     |Система|
         : Завершує взаємодію;
         stop;

@enduml

</center>

- ID: v1.NOT_LOGGED.EX.001

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;" >

@startuml

    left header
         <font color=000 size=10><b>ID:</b> v1.NOT_LOGGED.EX.001
         <font color=000 size=10><b>НАЗВА:</b> Відхилити запит на реєстрацію
         <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
         <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
         <font color=000 size=10>Користувач не зареєстрований у системі.
         <font color=000 size=10>Клієнт надіслав хибні дані реєстрації.
         <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про відхилення реєстрації
     end header

     |Система|
         start
         : Надає користувачу повідомлення
         про відхилення реєстрації;

     |Користувач|
         : Отримує повідомлення про
         відхилення реєстрації;

     |Система|
         : Завершує взаємодію;
         stop;

@enduml

</center>
           
- ID:	v1.NOT_LOGGED.EX.002

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;" >

@startuml

    left header
         <font color=000 size=10><b>ID:</b> v1.NOT_LOGGED.EX.002
         <font color=000 size=10><b>НАЗВА:</b> Відхилити спробу авторизації через помилку ідентифікації
         <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
         <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
         <font color=000 size=10>Користувач не авторизований у системі.
         <font color=000 size=10>Система не змогла ідентифікувати користувача.
         <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про помилку спроби авторизації
     end header

     |Система|
         start
         : Надає користувачу повідомлення про відхилення
         авторизації через помилку ідентифікації;

     |Користувач|
         : Отримує повідомлення про відхилення
         авторизації через помилку ідентифікації;

     |Система|
         : Завершує взаємодію;
         stop;

@enduml

</center>

- ID: v1.NOT_LOGGED.EX.003

<center style="
    border-radius:4px;
    border: 1px solid #cfd7e6;
    box-shadow: 0 1px 3px 0 rgba(89,105,129,.05), 0 1px 1px 0 rgba(0,0,0,.025);
    padding: 1em;" >

@startuml

    left header
         <font color=000 size=10><b>ID:</b> v1.NOT_LOGGED.EX.003
         <font color=000 size=10><b>НАЗВА:</b> Відхилити спробу авторизації через помилку аутентифікації
         <font color=000 size=10><b>УЧАСНИКИ:</b> Користувач, Система
         <font color=000 size=10><b>ПЕРЕДУМОВИ:</b>
         <font color=000 size=10>Клієнт не авторизований у системі.
         <font color=000 size=10>Система не змогла аутентифікувати користувача.
         <font color=000 size=10><b>РЕЗУЛЬТАТ:</b> Повідомлення про спроби авторизації
     end header

     |Система|
         start
         : Надає користувачу повідомлення про відхилення
         авторизації через помилку аутентифікації;

     |Користувач|
         : Отримує повідомлення про відхилення
         авторизації через помлку аутентифікації;

     |Система|
         : Знижує ступінь довіри до користувача;

         : Завершує взаємодію;
         stop;

@enduml

</center>
