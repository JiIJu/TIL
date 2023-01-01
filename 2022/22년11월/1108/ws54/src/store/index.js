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
    optionList : [
      {
        type:'샷',
        price: 500,
        count : 0,
      },
      {
        type:'펄',
        price: 800,
        count : 0,
      },
      {
        type:'캡사이신 한바퀴',
        price: 1500,
        count : 0,
      },
    ]
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      let totalPrice = 0
      state.orderList.forEach((order)=> {
        totalPrice += order.menu.price+order.size.price
        // console.log(order.menu.price)
      })
      
      return totalPrice
    },
    sumOption(state) {
      let totalOption = 0
      state.optionList.forEach(option => {
        totalOption +=  option.count * option.price
      });
      return totalOption
    }
  },
  mutations: {
    addOrder: function (state) {
      state.menuList.forEach((menu)=> {
        if (menu.selected) {
          state.sizeList.forEach((size)=> {
            if (size.selected) {
              state.orderList.push({menu,size})
              menu.selected = false
              size.selected = false
            }
          })
          
        }
      })
      console.log(state.orderList)
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
    updateOptionList: function (state,newOption) {
      state.optionList.forEach((option) => {
        if (option.type === newOption.type) {
          option.count += 1
        }
      })
    },
    decreaseUpdateOptionList: function (state,newOption) {
      state.optionList.forEach((option) => {
        if (option.type === newOption.type) {
          option.count -= 1
        }
      })
    },
    optionZero: function (state) {
      state.optionList.forEach((option) => {
        option.count = 0
      })
    }
    
  },
  actions: {
    pickMenu(context,menu) {
      context.commit('updateMenuList',menu)

    },
    pickSize(context,menu) {
      context.commit('updateSizeList',menu)

    },
    order(context) {
      context.commit('addOrder')
    },
    increase(context,option) {
      context.commit('updateOptionList',option)
    },
    decrease(context,option) {
      context.commit('decreaseUpdateOptionList',option)
    },
    option(context,option) {
      context.commit('sumOption',option)
    },
    optionzero(context) {
      context.commit('optionZero')
    }
  },
  modules: {
  }
})