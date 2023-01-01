import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {name : '아메리카노',
      price : 3000,
    selected : false,
    image: 'https://image.homeplus.kr/td/0428d446-db1f-4c0b-b99e-c244504a957e'},
    {name : '카페라떼',
      price : 4000,
    selected : false,
    image: 'https://image.homeplus.kr/td/50c57f2a-1929-4bf7-848d-fbb58922cf1e'},
    {name : '도피',
      price : 6000,
    selected : false,
    image: 'https://emmaru.com/matzip/include/pics/2022/05/10/m_28068L202051_10.jpg'
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
    addOrder: function (state) {
      state.menuList.forEach((menu)=> {
        if (menu.selected === true) {
          state.sizeList.forEach((size)=> {
            if (size.selected === true) {
              state.orderList.push({menu,size})
              menu.selected = false
              size.selected = false
            }
          })
        }
      })

    },
    updateMenuList: function (state,selectedMenu) {
      state.menuList.forEach((menu) => {
        if (menu.name === selectedMenu.name) {
          menu.selected = !menu.selected
        }
      })
    },
    updateSizeList: function (state,selectedSize) {
      state.sizeList.forEach((size) => {
        if (size.name === selectedSize.name) {
          size.selected = !size.selected
        }
      })
    },
  },
  actions: {
    pickMenu(context,menu) {
      context.commit('updateMenuList',menu)
      console.log(menu)
    },
    pickSize(context,menu) {
      context.commit('updateSizeList',menu)
      console.log(menu)
    }
  },
  modules: {
  }
})