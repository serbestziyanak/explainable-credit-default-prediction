# GitHub'a yükleme ve Zenodo'dan DOI alma rehberi

Bu paket, daha önce oluşturulan **`serbestziyanak/explainable-credit-default-prediction`** deposunun güncellenmiş makale deneyleri için hazırlanmıştır.

## GitHub'a yükleme

1. ZIP dosyasını bilgisayarınızda açın. İçindeki **`README.md`, `CITATION.cff`, `requirements.txt`, `notebooks/`, `results/`, `figures/`, `docs/`, `scripts/` ve `environment/`** içeriklerini GitHub deposunun **kök dizinine** yükleyin. Depo kökünde ikinci bir gereksiz `explainable-credit-default-prediction/` klasörü oluşturmamaya dikkat edin.
2. Mevcut `README.md` eski deneyleri anlatıyorsa güncelleyin. Yeni notebook'ları `notebooks/` altına koyun. Önceki sürümleri korumak isterseniz `archive/legacy/` gibi belirgin bir klasöre taşıyın, ancak bunları nihai makalenin reprodüksiyon kaynağı olarak göstermeyin.
3. **`results/` içindeki üç ZIP dosyasını da yükleyin.** Bunlar önceki Colab PAPER deneylerinin sonuçlarıdır ve kodu yeniden çalıştırmadan makalenin bulgularını incelemeyi sağlar.
4. `CITATION.cff` dosyasındaki yazar(lar) ve önerilen `version: 2.0.0` bilgisini kontrol edin. Katkıda bulunan başka kişiler varsa ekleyin; ORCID numarası varsa kendi numaranızı kullanın. Gerçekten seçmediğiniz bir lisansı eklemeyin.
5. `README.md` içindeki yeni çalışma DOI alanı **bilerek boş** bırakılmıştır. Daha önceki **10.5281/zenodo.23010902** DOI'si eski bir arşive aittir; yeni sonuçların DOI'si olarak kullanmayın.
6. Yeni GitHub dosyaları commit edildikten sonra önce depo içeriğini ve `python scripts/validate_archives.py` sonucunu gözden geçirin.

## Zenodo üzerinde yeni sürüm DOI'si almak

**Önerilen yol: Mevcut GitHub–Zenodo bağlantısını kullanarak yeni GitHub Release oluşturmak.**

1. Zenodo hesabınızda oturum açın. Profil menüsü altındaki **GitHub** bölümünü açın ve **Sync now** seçeneğini kullanın.
2. Mevcut deponun bağlantısının etkin (`enabled`) olduğunu kontrol edin. Önceki DOI'nin aynı GitHub deposuna ait olup olmadığını, hesabınızdaki kayıt üzerinden doğrulayın.
3. GitHub deponuzun **Releases → Draft a new release** bölümünde yeni, daha önce kullanılmamış bir etiket oluşturun; önerilen etiket **`v2.0.0`** (mevcut sürüm sırasına uyuyorsa).
4. Release başlığına örneğin `Credit risk calibration and explanation robustness — v2.0.0` yazın. Açıklamaya yeni iki-veri-kümeli deneyleri, kalibrasyon ve XAI sağlamlık analizlerini ekleyin. **Publish release** ile yayımlayın.
5. Zenodo'nun bu yeni GitHub release'ini arşivlemesini bekleyin. Zenodo'nun gösterdiği **yeni sürüme özgü DOI**'yi kopyalayın. Oluşturulma tamamlanmadan DOI tahmin etmeyin.
6. Yeni DOI'yi makalenin **Data and Code Availability** bölümüne ekleyin. Önceki DOI'yi gerektiğinde *önceki sürüm* olarak ayrıca anabilirsiniz.
7. İsterseniz GitHub `README.md` dosyasına Zenodo'nun oluşturduğu DOI rozeti ekleyin. **Dikkat:** Release oluşturulduktan sonraki README değişiklikleri arşivlenmiş release'e otomatik olarak eklenmez; tam olarak arşivlenecek sürümü release'den **önce** tamamlayın.

**Sürüm DOI / tüm sürümler DOI:** Zenodo'da aynı yazılımın her yayımlanan sürümü farklı DOI alabilir; arşiv ekranında ayrıca tüm sürümler için bir kavram DOI'si bulunabilir. Makalenizde kullanılan **belirli kod/sonuç sürümünü** tanımlamak için sürüme özgü DOI'yi kullanın.

## Makalede önerilen İngilizce açıklama (DOI alındıktan sonra)

> The code, analysis notebooks, and the three PAPER-mode output archives supporting this study are publicly available at https://github.com/serbestziyanak/explainable-credit-default-prediction and preserved in Zenodo (version-specific DOI: **[INSERT THE NEW DOI]**). The credit datasets were retrieved from the UCI Machine Learning Repository (IDs 350 and 573).

Bu bir **şablondur**; yeni Zenodo DOI gerçekten oluşturulunca köşeli parantezli kısmı değiştirin.

## Bilimsel ve telif konuları

- Henüz kaynak kod lisansı seçilmedi. Yayınlamadan önce kodu MIT gibi bir lisansla paylaşmak isteyip istemediğinize **siz** karar vermelisiniz. Lisans koymadan herkese açık yayımlamakla açık kaynak lisans vermek aynı şey değildir.
- Önceki GitHub/Zenodo arşivini güncel deneyleri içeriyormuş gibi sunmayın. Yeni bir sürüm yayımlayın.
- Derginiz **çift kör hakemlik** istiyorsa GitHub kullanıcı adınız, Zenodo üretici adı ve DOI yoluyla kimliğinizin açıklanması konusunda derginin paylaşım kurallarını kontrol edin.
- Daha sonra aynı dosyaları tekrar **ayrı bir yeni Zenodo deposu** olarak yayımlamak yerine, mevcut GitHub–Zenodo sürüm zincirinden devam etmek daha tutarlı olabilir; bu seçimin doğruluğunu önceki Zenodo kaydınızın bağlantılarına bakarak teyit edin.

Resmî yönergeler: [Zenodo – GitHub repo etkinleştirme](https://help.zenodo.org/docs/github/enable-repository/) · [GitHub release arşivleme](https://help.zenodo.org/docs/github/archive-software/github-upload/) · [CITATION.cff kullanımı](https://help.zenodo.org/docs/github/describe-software/citation-file/).
