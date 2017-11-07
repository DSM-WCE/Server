const request = require('request');
const cheerio = require('cheerio');


/**
 *  실시간 차트를 파싱하여 josn객체로 반환하는 함수 getCurrentChart()
 */
function getCurrentChart(callback) {
    var url = 'https://music.bugs.co.kr/chart/track/day/total';

    request(url, function (err, response, html) {
        if(err) { throw err; }

        var $ = cheerio.load(html);
        var currentChart = new Array();
        var songInfo = new Object();

        for(var i=0; i<100; i++) {
            songInfo.title = $('p.title > a').eq(i).text();
            songInfo.artist = $('p.artist > a:not(.more)').eq(i).text();
            currentChart.push(songInfo);
            songInfo = new Object();
        }
        callback(currentChart);
    });
}

function removeSpaces(arr) {
    if(arr.length > 0) {
        for (var index in arr) {
            if ((arr.indexOf('') !== -1) || (arr.indexOf(' ') !== -1) || (arr.indexOf('  ') !== -1)) {
                if ((arr[index].length === 0) || (arr[index] === ' ')) {
                    arr.splice(index, 1);
                }
            } else {
                return;
            }
        }
    } else {
        return;
    }
    removeSpaces(arr);
}

getCurrentChart((data) => {
    console.log(data);
});