<template>
  <div class="border">
    <h1>싸피 이거는 내가 만든 새로운 컴포넌트다!</h1>
    <MyComponentItem 
      static-props="레전드 전설의 레전드 엄마미투사경영수영복"
      :dynamic-props="dynamicProps"
      @child-to-parent = 'parentGetEvent'
      @child-input="getDynamicData"
      />
    
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  data : function() {
    return {
      dynamicProps : '이건 동적인 데이터!'
    }
  },
  methods : {
      parentGetEvent: function(childData) {
        console.log('자식컴포넌트에서 발생한 emit이벤트를 받아브렀당께')
        console.log(childData)
        this.$emit('아아아악!!',childData)
      } ,
      getDynamicData : function(childInputData) {
        console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
      }
    },
}
</script>
<style>
  .border {
    border: solid 1px black;
  }
</style>
