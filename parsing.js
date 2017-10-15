const request = require('request');
const cheerio = require('cheerio');


/**
 *  실시간 차트를 파싱하여 josn객체로 반환하는 함수 getCurrentChart()
 */
function getCurrentChart(callback) {
    var url = 'http://music.bugs.co.kr/chart?wl_ref=M_left_02_01';
    var currentChart;

    request(url, function (err, response, html) {
        if (err) {
            throw err;
        }
        /* html 소스를 파싱 */
        var $ = cheerio.load(html);
        var artist = $("p.artist").text().trim().split('\n');
        /* 가수를 파싱 */
        var name = $('p.title').text().trim().split('\n');
        /* 중복 제거를 위해 중복된 가수 배열 */
        var overlap = $("a.more").text().trim().split('\n');

        /* 공백 제거 */
        removeSpaces(name);
        removeSpaces(artist);

        /* 중복 제거 */
        // code
    });
}

/**
 * 배열의 공백을 제거해주는 함수 removeSpaces()
 */
function removeSpaces(arr) {
    for (var index in arr) {
        if ((arr.indexOf('') !== -1) || (arr.indexOf(' ') !== -1) || (arr.indexOf('  ') !== -1)) {
            if ((arr[index].length === 0) || (arr[index] === ' ')) {
                arr.splice(index, 1);
            }
        } else {
            return arr;
        }
    }
    removeSpaces(arr);
}

/**
 * 중복 방향을 나타는 함수
 */
function checkOverlap(arr, index) {
    if(arr[index] === arr[index+1] || arr[index] === arr[index-1])
        return true;
    else
        return false;
}

getCurrentChart();
