const request = require('request');
const cheerio = require('cheerio');
const download = require('download-file');


/**
 *  일간 차트의 앨범 사진을 다운하는 함수 getAlbumArt()
 */
function getAlbumArt() {
    let url = 'https://music.bugs.co.kr/chart/track/day/total';
    const saveDir = __dirname + "/public/images";

    request(url, (err, response, html) => {
        if(err) { throw err; }

        let $ = cheerio.load(html);

        for(let i=0; i<100; i++) {
            let fileName = i + 1;
            let url = $('a.thumbnail > img').eq(i).attr('src');

            let options = {
                directory: saveDir,
                filename: fileName + '.png'
            }

            download(url, options, (err) => {
                if(err) { throw err; }
            });
        }
    });
}
