import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {title : '아메리카노',
      price : 3000,
    selected : false,
    image: 'https://image.homeplus.kr/td/0428d446-db1f-4c0b-b99e-c244504a957e'},
    {title : '카페라떼',
      price : 4000,
    selected : false,
    image: 'https://image.homeplus.kr/td/48c14910-5f1c-4294-95de-8f64f581f503'},
    {title : '도피',
      price : 6000,
    selected : false,
    image: 'https://www.google.com/imgres?imgurl=https%3A%2F%2Femmaru.com%2Fmatzip%2Finclude%2Fpics%2F2022%2F05%2F10%2Fm_28068L202051_10.jpg&imgrefurl=https%3A%2F%2Femmaru.com%2Fmatzip%2Fmatzip.do%3Fcode%3DM220510201423028068L&tbnid=v4lkTLeHMPxdvM&vet=12ahUKEwiqidSwpZ37AhVLXJQKHVa1Bk4QMygOegUIARCUAQ..i&docid=l0LwnvcuyeRYFM&w=600&h=449&q=%EB%8F%99%EB%AA%85%EB%8F%99%20%EB%8F%84%ED%94%BC&ved=2ahUKEwiqidSwpZ37AhVLXJQKHVa1Bk4QMygOegUIARCUAQ'
    }
    ],
    sizeList: [
      {name:'small',
      price:500,
      selected : false},
      {name:'mid',
      price:1000,
      selected : false}
      ,{name:'large',
      price:1500,
      selected : false}
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function (state,selectedMenu) {
      selectedMenu.forEach((menu)=> {
        if (menu.selected) {
          state.orderList.push(menu)
        }
      })
    },
    updateMenuList: function (state,selectedMenu) {
      state.menuList.forEach((menu) => {
        if (menu.selected === selectedMenu.selected) {
          menu.selected = true
        }
      })
    },
    updateSizeList: function (state,selectedSize) {
      state.sizeList.forEach((menu) => {
        if (menu.selected === selectedSize.selected) {
          menu.selected = true
        }
      })
    },
  },
  actions: {
  },
  modules: {
  }
})