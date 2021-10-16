/**
 * Jual Beli CLI. @isywl_
 * Ketentuan: total >= 100.000 maka diskon 10% bila kurang diskon 5%
 **/

const { stdin, stdout } = process
const rl = require('readline').createInterface(stdin, stdout)

const q = q => new Promise(resolve => {
    rl.question(q, ans => resolve(ans))
})

;(async function() {
    // tambah data barang disini
    const barang = {
        susu: 50000,
        coklat: 15000,
        aqua: 20000,
        sabun: 35500,
    }

    // menampikkan data produk
    function tampilProduk() {
        return `[${Object.keys(barang).join` `}]`
    }

    var total = 0;
    var tampung = []

    // asyncronous question
    async function tanya() {
        try {
            let beli = await q(`\n? Mau beli apa ka ? ketik N jika tidak ada. ${tampilProduk()}: `)
            if (beli.toLowerCase() == 'n') return process.exit()
            if (!(beli in barang)) {
                console.log(`\n! Barang ${beli} tidak ada dalam database!`)
                process.exit()
            }
            total += barang[beli]
            tampung.push(beli)

            let diskon = total >= 100000 ? (total - (total*(10/100))) : (total - (total*(5/100)))
            let list = `\n`

            for (i in tampung) {
               list += `  # ${tampung[i].split` `.map(v => v.charAt(0).toUpperCase() + v.slice(1)).join` `}: Rp. ${barang[tampung[i]]}\n`
            }
            let print = `
% Rincian Harga:
- Barang: ${list}
- Potongan Harga: ${total >= 100000 ? `${total*(10/100)} 10%` : `${total*(10/100)} 5%`}
- Total: Rp. ${(diskon).toLocaleString('ID-id')}
            `
            console.log(print)
            tanya()
        } catch(e) {
            console.log('! Pembelian dibatalkan', e)
        }
    }
    await tanya()
})()
