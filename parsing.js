const request = require('request');
const cheerio = require('cheerio');


/**
 *  실시간 차트를 파싱하여 josn객체로 반환하는 함수 getCurrentChart()
 */
function getCurrentChart(callback) {
    var url = 'http://music.naver.com/listen/top100.nhn?domain=TOTAL&duration=1h';
    var chart = null;

    request(url, function (err, response, html) {
        if(err) { throw err; }

        var $ = cheerio.load(html);
        var name = $('td.name').text().trim().replace(/\t+/g, "").split('\n');
        var artistName = $('a._artist').text().trim().replace(/\t+/g, "").split('\n');

        removeSpaces(name);
        removeSpaces(artistName);
        name.splice(0, 3);

        var currentChart = new Array();
        var songInfo = new Object();
        for(var i=0; i<50; i++) {
            songInfo.title = name[i];
            songInfo.artist = artistName[i];
            currentChart.push(songInfo);
            songInfo = new Object();
        }
        chart = JSON.stringify(currentChart);
    });
    /*callback(chart);*/
}

function removeSpaces(arr) {
    for (var index in arr) {
        if ((arr.indexOf('') !== -1) || (arr.indexOf(' ') !== -1) || (arr.indexOf('  ') !== -1)) {
            if ((arr[index].length === 0) || (arr[index] === ' ')) {
                arr.splice(index, 1);
            }
        } else {
            return;
        }
    }
    removeSpaces(arr);
}
