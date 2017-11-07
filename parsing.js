const request = require('request');
const cheerio = require('cheerio');


/**
 *  실시간 차트를 파싱하여 josn객체로 반환하는 함수 getCurrentChart()
 */
function getCurrentChart(callback) {
    let url = 'https://music.bugs.co.kr/chart/track/day/total';

    request(url, (err, response, html) => {
        if(err) { throw err; }

        let $ = cheerio.load(html);
        let currentChart = new Array();
        let songInfo = new Object();

        for(let i=0; i<100; i++) {
            songInfo.title = $('p.title > a').eq(i).text();
            songInfo.artist = $('p.artist > a:not(.more)').eq(i).text();
            currentChart.push(songInfo);
            songInfo = new Object();
        }
        callback(currentChart);
    });
}