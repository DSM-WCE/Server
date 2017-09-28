const request = require('request');
const cheerio = require('cheerio');


/**
 *  실시간 차트를 파싱하여 josn객체로 반환하는 함수 getCurrentChart()
 */
function getCurrentChart(callback) {
    var url = 'http://music.bugs.co.kr/chart?wl_ref=M_left_02_01';
    var currentChart;
    
    request(url, function(err,response, html) {
        /* HTML소스를 크롤링 */
        if(err) {
            throw err;
        }
    
        /* 노래 제목을 순서대로 파싱 */
        var $ = cheerio.load(html);
        var result = $("p.title").text();
        var music_name = result.trim();
    
        /* 가수를 파싱 */
        var temp = $('p.artist').text();
        var artist_name = temp.trim();
    
        /* 가수와 노래 제목을 배열에 넣음 */
        var overrap = $("a.more").text().trim().split('\n');
        var name = music_name.split('\n');
        var artist = artist_name.split('\n');
    
        for(var i in overrap) { // 아티스트 더 보기로인해 생기는 가수 중복을 제거
            if(artist.indexOf(overrap[i]) != -1) {
                artist.splice(artist.indexOf(overrap[i]), 1);
            }
        }
        removeSpaces(name);
        removeSpaces(artist);

        // callback(currentChart); // 최종 차트 정보를 담은 JSON object를 callback을 통해 반환
    });
}

/**
 * 배열의 공백을 제거해주는 함수 removeSpaces()
 */
function removeSpaces(arr) {
    for(var index in arr) {
        if((arr.indexOf('') != -1) || (arr.indexOf(' ') != -1)) {
            if((arr[index].length == 0) || (arr[index] === ' ')) {
                arr.splice(index, 1);
            }
        } else {
            return arr;
        }
    }
    removeSpaces(arr);
}

getCurrentChart();