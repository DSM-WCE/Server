const request = require('request');
const cheerio = require('cheerio');
const download = require('download-file');
const fs = require('fs');


// 이미지파일 저장 디렉토리
const path = __dirname + "/public/images";
/**
 *  일간 차트의 앨범 사진을 다운하는 함수 getAlbumArt()
 */
function getAlbumArt() {
    let url = 'https://music.bugs.co.kr/chart/track/day/total';

    request(url, (err, response, html) => {
        if(err) { throw err; }

        let $ = cheerio.load(html);

        for(let i=0; i<100; i++) {
            let fileName = i + 1;
            let url = $('a.thumbnail > img').eq(i).attr('src');

            let options = {
                directory: path,
                filename: fileName + '.png'
            };

            download(url, options, (err) => {
                if(err) { throw err; }
            });
        }
    });
}

function deleteAllImage() {
    for(let i=0; i<100; i++) {
        let file = path + '/' + (i+1) + '.png';
        fs.unlink(file, (err) => {
            if(err) { throw err; }
        });
    }
}