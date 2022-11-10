const state = function () {
  return {
    list: [
      {
        id: 1638771553377,
        content: "Vue",
        dueDateTime: "2021-12-11T16:05",
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 1638771553378,
        content: "Vue Router",
        dueDateTime: "2021-12-11T16:05",
        isCompleted: false,
        isImportant: true,
      },
      {
        id: 16387715533779,
        content: "Vuex",
        dueDateTime: "2021-12-11T16:05",
        isCompleted: true,
        isImportant: false,
      },
    ],
  };
};

const getters = {};
const mutations = {};
const actions = {};

export default {
  // module 구분을 위한 이름 설정 옵션
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
