/* 
  아래에 코드를 작성해주세요.
*/

const URL_API = 'https://ws.audioscrobbler.com/2.0/?method=track.search&track=Believe&api_key=5746c2c7ad22f6f9d6577e714c0a138b&format=json'
const inputTag = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box__button')

let albums = new Array()


searchBtn.addEventListener('click',function fetchAlbums(page,limit) {
  let keyword = inputTag.value
  // inputTag.value = ''

  axios({
    method : 'get',
    url : URL_API,
  })
  .then(response => {
    response.data.results.trackmatches.track.forEach(res => {
      if (res.name.includes(keyword))
      {
      albums.push(res)}
      // return albums
    });
    // console.log(response.data.results.trackmatches)
    const divTag0 = document.querySelector('.search-result')
  
  albums.forEach(music => {
    const divTag1 = document.createElement('div')
  divTag1.setAttribute('class','search-result__card')
  divTag0.appendChild(divTag1)
    const divTag2 = document.createElement('div')
    const card = document.createElement('div')
    card.classList.add('search-result__card')
    const cardImg = document.createElement('img')
    cardImg.src = music.image[1]['#text']
    // console.log(music.image[1]['#text'])
    card.append(cardImg)
    divTag1.append(cardImg)
    divTag2.setAttribute('class','search-result__text')
    divTag1.appendChild(divTag2)
    const h2Tag = document.createElement('h2')
    const pTag = document.createElement('p')
    h2Tag.innerText = music.artist
    pTag.innerText = music.name
    divTag2.appendChild(h2Tag)
    divTag2.appendChild(pTag)
    
    // divTag1.append(divTag2)
    
  })
  })
  .catch(response =>{
    alert('잠시후 다시 시도해주세요')
  })
  
})



