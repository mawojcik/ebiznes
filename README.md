**Zadanie 1** Docker

:white_check_mark: 3.0 3.0 obraz ubuntu z Pythonem w wersji 3.10 [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/b3ba114e41052bc9353fc45405809b8c793006c4)

:white_check_mark: 3.5 obraz ubuntu:24.02 z Javą w wersji 8 oraz Kotlinem[Link do commita2 ](https://github.com/mawojcik/ebiznes/commit/bf24fd31f587333069b6d59b8eb6e2e0a33950dd)

:white_check_mark: 4.0 do powyższego należy dodać najnowszego Gradle’a oraz paczkę JDBC SQLite w ramach projektu na Gradle (build.gradle) [Link do commita 3](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)

:white_check_mark: 4.5 stworzyć przykład typu HelloWorld oraz uruchomienie aplikacji przez CMD oraz gradle [Link do commita 4](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)

:white_check_mark: 5.0 dodać konfigurację docker-compose[Link do commita 5](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)


Kod: [exercise1](https://github.com/mawojcik/ebiznes/tree/main/exercise1)

**Zadanie 2** Framework Play and Scala

:white_check_mark: 3.0 Należy stworzyć kontroler do Produktów [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/b3ba114e41052bc9353fc45405809b8c793006c4)

:white_check_mark: 3.5 Do kontrolera należy stworzyć endpointy zgodnie z CRUD - dane pobierane z listy [Link do commita2 ](https://github.com/mawojcik/ebiznes/commit/bf24fd31f587333069b6d59b8eb6e2e0a33950dd)

:x: 4.0 Należy stworzyć kontrolery do Kategorii oraz Koszyka + endpointy
zgodnie z CRUD [Link do commita 3](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)

:x: 4.5 Należy aplikację uruchomić na dockerze (stworzyć obraz) oraz dodać
skrypt uruchamiający aplikację via ngrok [Link do commita 4](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)

:x: 5.0 Należy dodać konfigurację CORS dla dwóch hostów dla metod CRUD [Link do commita 5](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)


Kod: [exercise2](https://github.com/mawojcik/ebiznes/tree/main/exercise2)


**Zadanie 3** Kotlin

:white_check_mark: 3.0 Należy stworzyć aplikację kliencką w Kotlinie we frameworku Ktor, która pozwala na przesyłanie wiadomości na platformę Discord [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/9b9834d981aeef758c7701e033568477d4094aba)

:x: 3.5 Aplikacja jest w stanie odbierać wiadomości użytkowników z platformy Discord skierowane do aplikacji (bota) [Link do commita2](https://github.com/mawojcik/ebiznes/commit/bf24fd31f587333069b6d59b8eb6e2e0a33950dd)

:x: 4.0 Zwróci listę kategorii na określone żądanie użytkownika [Link do commita 3](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)

:x: 4.5 Zwróci listę produktów wg żądanej kategorii [Link do commita 4](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)

:x: 5.0 Aplikacja obsłuży dodatkowo jedną z platform: Slack, Messenger, Webex [Link do commita 5](https://github.com/mawojcik/ebiznes/commit/7cd71d8f2c11e92063f3e71dcef75eccc5685838)


Kod: [exercise3](https://github.com/mawojcik/ebiznes/tree/main/zadanie3)


**Zadanie 4** Go

:white_check_mark: 3.0 Należy stworzyć aplikację we frameworki echo w j. Go, która będzie miała kontroler Produktów zgodny z CRUD [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/4cb379cc31073d4bdd4d4864aff8d3ed77f332b0)

:white_check_mark: 3.5 Należy stworzyć model Produktów wykorzystując gorm oraz wykorzystać model do obsługi produktów (CRUD) w kontrolerze (zamiast listy) [Link do commita2](https://github.com/mawojcik/ebiznes/commit/4cb379cc31073d4bdd4d4864aff8d3ed77f332b0)

:white_check_mark: 4.0 4.0 Należy dodać model Koszyka oraz dodać odpowiedni endpoint [Link do commita 3](https://github.com/mawojcik/ebiznes/commit/4cb379cc31073d4bdd4d4864aff8d3ed77f332b0)

:white_check_mark: 4.5 Należy stworzyć model kategorii i dodać relację między kategorią, a produktem [Link do commita 4](https://github.com/mawojcik/ebiznes/commit/4cb379cc31073d4bdd4d4864aff8d3ed77f332b0)

:white_check_mark: 5.0 pogrupować zapytania w gorm’owe scope'y [Link do commita 5](https://github.com/mawojcik/ebiznes/commit/e149b62ef9db3af140f0f18a90e1ca99056affa5)


Kod: [exercise4](https://github.com/mawojcik/ebiznes/tree/main/exercise4)

Nagranie:

https://github.com/user-attachments/assets/7f539d85-2463-4d1a-aba7-fb8941d1bc48

**Zadanie 5** Frontend

:white_check_mark: 3.0 W ramach projektu należy stworzyć dwa komponenty: Produkty oraz Płatności; Płatności powinny wysyłać do aplikacji serwerowej dane, a w Produktach powinniśmy pobierać dane o produktach z aplikacji serwerowej [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/87cf27a92953c40fe1fc3139033e257dc6d15621)

:white_check_mark: 3.5 Należy dodać Koszyk wraz z widokiem; należy wykorzystać routing [Link do commita2](https://github.com/mawojcik/ebiznes/commit/ecb6c94bbb9808dbc5a464f97b63723a53c219f6)

:white_check_mark: 4.0 Dane pomiędzy wszystkimi komponentami powinny być przesyłane za pomocą React hooks [Link do commita 3](https://github.com/mawojcik/ebiznes/commit/ecb6c94bbb9808dbc5a464f97b63723a53c219f6)

:x: 4.5 Należy dodać skrypt uruchamiający aplikację serwerową oraz kliencką na dockerze via docker-compose [Link do commita 4](https://github.com/mawojcik/ebiznes)

:x: 5.0 Należy wykorzystać axios’a oraz dodać nagłówki pod CORS [Link do commita 5](https://github.com/mawojcik/ebiznes)


Kod: [exercise5](https://github.com/mawojcik/ebiznes/tree/main/exercise5/shopapp)

Nagranie:

https://github.com/user-attachments/assets/1ed53a77-3214-4025-8671-f4ba9d85edcb

**Zadanie 6** Testy

:white_check_mark: 3.0 Należy stworzyć 20 przypadków testowych w CypressJS lub Selenium (Kotlin, Python, Java, JS, Go, Scala) [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/08391da86151b72027ca7418643e26b9c7425e3d)

:white_check_mark: 3.5 Należy rozszerzyć testy funkcjonalne, aby zawierały minimum 50 asercji [Link do commita2](https://github.com/mawojcik/ebiznes/commit/08391da86151b72027ca7418643e26b9c7425e3d)

:x: 4.0 Należy stworzyć testy jednostkowe do wybranego wcześniejszego projektu z minimum 50 asercjami [Link do commita 3](https://github.com/mawojcik/ebiznes/)

:x: 4.5 Należy dodać testy API, należy pokryć wszystkie endpointy z minimum jednym scenariuszem negatywnym per endpoint [Link do commita 4](https://github.com/mawojcik/ebiznes)

:x: 5.0 Należy uruchomić testy funkcjonalne na Browserstacku [Link do commita 5](https://github.com/mawojcik/ebiznes)


Kod: [exercise6](https://github.com/mawojcik/ebiznes/tree/main/exercise6)

**Zadanie 7** Sonar

:white_check_mark: 3.0 Należy dodać litera do odpowiedniego kodu aplikacji serwerowej w hookach gita [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/79ddfc30d93531962a15102742a739e28c4ecef1)

:white_check_mark: 3.5 Należy wyeliminować wszystkie bugi w kodzie w Sonarze (kod aplikacji serwerowej) [Link do commita2](https://github.com/mawojcik/ebiznes/commit/79ddfc30d93531962a15102742a739e28c4ecef1)

:x: 4.0 Należy wyeliminować wszystkie zapaszki w kodzie w Sonarze (kod aplikacji serwerowej) [Link do commita 3](https://github.com/mawojcik/ebiznes/)

:x: 4.5 Należy wyeliminować wszystkie podatności oraz błędy bezpieczeństwa w kodzie w Sonarze (kod aplikacji serwerowej) [Link do commita 4](https://github.com/mawojcik/ebiznes)

:x: 5.0 Należy wyeliminować wszystkie błędy oraz zapaszki w kodzie aplikacji klienckiej [Link do commita 5](https://github.com/mawojcik/ebiznes)


Kod: [exercise7](https://github.com/mawojcik/ebiznes/tree/main/exercise7)

**Zadanie 8** Oauth2

:white_check_mark: 3.0 logowanie przez aplikację serwerową (bez Oauth2) [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/32d01b0ac6f37595d60220b398d621712d525d30)

:white_check_mark: 3.5 rejestracja przez aplikację serwerową (bez Oauth2) [Link do commita2](https://github.com/mawojcik/ebiznes/commit/32d01b0ac6f37595d60220b398d621712d525d30)

:white_check_mark: 4.0 logowanie via Google OAuth2 [Link do commita 3](https://github.com/mawojcik/ebiznes/commit/65c1b43694e3844f0cc91ac837a8152b526d7d62)

:white_check_mark: 4.5 logowanie via Facebook lub Github OAuth2 [Link do commita 4](https://github.com/mawojcik/ebiznes/commit/b1c7f1a9825e59e4a25eb55f509db0885b0d4c7c)

:white_check_mark: 5.0 zapisywanie danych logowania OAuth2 po stronie serwera [Link do commita 5](https://github.com/mawojcik/ebiznes/commit/b1c7f1a9825e59e4a25eb55f509db0885b0d4c7c)


Kod: [exercise8](https://github.com/mawojcik/ebiznes/tree/main/exercise8)

Nagranie:



https://github.com/user-attachments/assets/6dac034e-bf5b-42c8-b1e4-e3b21c8f8bf5


**Zadanie 9** bot

:white_check_mark: należy stworzyć po stronie serwerowej osobny serwis do łącznia z chatGPT do usługi chat [Link do commita 1](https://github.com/mawojcik/ebiznes/commit/5e8b3bf6fb7e5a1b50b39e4a5c51574514f36343)

:white_check_mark: 3.5 należy stworzyć interfejs frontowy dla użytkownika, który komunikuje się z serwisem; odpowiedzi powinny być wysyałen do frontendowego interfejsu [Link do commita2](https://github.com/mawojcik/ebiznes/commit/5e8b3bf6fb7e5a1b50b39e4a5c51574514f36343)

:white_check_mark: 4.0 stworzyć listę 5 różnych otwarć oraz zamknięć rozmowy [Link do commita 3](https://github.com/mawojcik/ebiznes/commit/10f15ec5b12d86b6789767cb669f9f008249b170)

:white_check_mark: 4.5 filtrowanie po zagadnieniach związanych ze sklepem (np. ograniczenie się jedynie do ubrań oraz samego sklepu) do GPT [Link do commita 4](https://github.com/mawojcik/ebiznes/commit/10f15ec5b12d86b6789767cb669f9f008249b170)

:x: 5.0 filtrowanie odpowiedzi po sentymencie [Link do commita 5](https://github.com/mawojcik/ebiznes/commit/b1c7f1a9825e59e4a25eb55f509db0885b0d4c7c)


Kod: [exercise9](https://github.com/mawojcik/ebiznes/tree/main/exercise9)

Nagranie:

https://github.com/user-attachments/assets/469f9713-aa0a-4c12-af48-2f35422f25c0

**Zadanie 10** Chmura

:white_check_mark: 3.0 Należy stworzyć odpowiednie instancje po stronie chmury na dockerze [Link do commita 1](https://github.com/mawojcik/ebiznes/tree/main/exercise10)

:x: 3.5 Stworzyć odpowiedni pipeline w Github Actions do budowania aplikacji (np. via fatjar) [Link do commita2](https://github.com/mawojcik/ebiznes/)

:x: 4.0 Dodać notyfikację mailową o zbudowaniu aplikacji [Link do commita 3](https://github.com/mawojcik/ebiznes/commit/)

:x: 4.5 Dodać krok z deploymentem aplikacji serwerowej oraz klienckiej na chmurę [Link do commita 4](https://github.com/mawojcik/ebiznes/)

:x: 5.0 Dodać uruchomienie regresyjnych testów automatycznych (funkcjonalnych) jako krok w Actions [Link do commita 5](https://github.com/mawojcik/ebiznes/)


Kod: [exercise10](https://github.com/mawojcik/ebiznes/tree/main/exercise10)

Nagranie:

https://github.com/user-attachments/assets/82a7ab49-e9d4-46a5-8554-915302ba2e0d


