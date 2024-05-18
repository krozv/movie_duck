import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/movies/MovieDetailView.vue'
import MovieListView from '@/views/movies/MovieListView.vue'
import RecommendView from '@/views/recommend/RecommendView.vue'
import MovieSearchView from '@/views/MovieSearchView.vue'
import SignUpView from '@/views/user/SignUpView.vue'
import LogInView from '@/views/user/LogInView.vue'
import ResultView from '@/views/recommend/ResultView.vue'
import { useCounterStore } from '@/stores/userStore'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'home',
      component: HomeView
    },
    {
      path:'/movies',
      name:'movies',
      component: MovieListView
    },
    {
      path:'/:movieId',
      name:'movie-detail',
      component: MovieDetailView
    },
    {
      path:'/movie-search/:search',
      name:'movie-search',
      component: MovieSearchView
    },
    {
      path:'/recommend',
      name:'recommend',
      component: RecommendView,
    },
    {
      path: '/recommend/result', 
      name: 'recommend-result', 
      component: ResultView,
      props: true,
    },
    // user 구현
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'ArticleView' && store.isLogin === false) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인이 되어있습니다.')
    return { name: 'ArticleView'}
  }
  // result로 이동 시 localStorage의 likedMovies 삭제
  if (to.name === 'recommend-result') {
    localStorage.removeItem('likedMovies')
  }
})

export default router
