// saat dokumen dimuat
$(document).ready(function() {
    // saat form submit
    $("#form-predict").submit(function(event) {
      // mencegah form untuk melakukan submit pada halaman sendiri
      event.preventDefault();
  
      // mengambil nilai input dari form
      var harapan_lama_sekolah = parseFloat($("#harapan_lama_sekolah").val());
      var pengeluaran_perkapita = parseFloat($("#pengeluaran_perkapita").val());
      var rerata_lama_sekolah = parseFloat($("#rerata_lama_sekolah").val());
      var usia_harapan_hidup = parseFloat($("#usia_harapan_hidup").val());
  
      // mengirim data input ke endpoint Flask untuk melakukan prediksi
      $.ajax({
        type: "POST",
        url: "/predict",
        contentType: "application/json",
        data: JSON.stringify({
          "harapan_lama_sekolah": harapan_lama_sekolah,
          "pengeluaran_perkapita": pengeluaran_perkapita,
          "rerata_lama_sekolah": rerata_lama_sekolah,
          "usia_harapan_hidup": usia_harapan_hidup
        }),
        success: function(result) {
          // menampilkan hasil prediksi ke dalam elemen dengan id "result"
          $("#result").text(result["prediksi"]);
        },
        error: function(xhr) {
          // menampilkan pesan error jika terjadi kesalahan saat melakukan request
          alert("Terjadi kesalahan saat melakukan request: " + xhr.status + " " + xhr.statusText);
        }
      });
    });
  });
  