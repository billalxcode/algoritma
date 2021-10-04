/**
 * Cari rata-rata nilai
 * @params {nilai} Array
 **/

/*
    Usage: rataRata(nilai); // 85
    var nilai = [70, 75, 80, 85, 90, 95, 100]
*/

module.exports.rataRata = (nilai = []) => eval(nilai.join`+`) / nilai.length
