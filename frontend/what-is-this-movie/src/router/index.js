import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieListView from '@/views/movies/MovieListView.vue'
import RecommendView from '@/views/recommend/RecommendView.vue'
import MovieSearchView from '@/views/MovieSearchView.vue'
import SignUpView from '@/views/user/SignUpView.vue'
import LogInView from '@/views/user/LogInView.vue'
import LogOutView from '@/views/user/LogOutView.vue'
import ProfileView from '@/views/user/ProfileView.vue'
import ResultView from '@/views/recommend/ResultView.vue'
import BoxOfficeDetailView from '@/views/movies/BoxOfficeDetailView.vue'
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
    // {
    //   path:'/:movieId',
    //   name:'movie-detail',
    //   component: MovieDetailView
    // },
    {
      path:'/:moviePk',
      name:'boxoffice-detail',
      component: BoxOfficeDetailView
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
    },
    {
      path: '/logout',
      name: 'LogOutView',
      component: LogOutView
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileView
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
  // result에서 나갈 시 localStorage의 likedMovies 삭제
  if (from.name === 'recommend-result') {
    localStorage.removeItem('likedMovies')
    // localStorage.removeItem('firstGenreMovies')
    // localStorage.removeItem('secondGenreMovies')
    // localStorage.removeItem('firstActorMovies')
    // localStorage.removeItem('secondActorMovies')
  }
  // sign up view에서 나갈 시 profile 이미지 불러오기
  if (from.name === 'SignUpView') {
    // axios로 user profilePath 요청
    // store.userProfile.value = profilePath
  }

})

export default router
