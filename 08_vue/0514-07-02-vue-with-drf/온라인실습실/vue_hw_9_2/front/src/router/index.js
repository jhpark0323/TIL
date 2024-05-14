import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '../views/ArticleCreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import { useArticleStore } from '../stores/articles'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/create',
      name: 'create',
      component: ArticleCreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
      beforeEnter: () => {
        const store = useArticleStore()
        if (store.isLogin) {
          return {name: 'home'}
        }
      }
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView,
      beforeEnter: () => {
        const store = useArticleStore()
        if (store.isLogin) {
          return {name: 'home'}
        }
      }
    }
  ]
})

export default router
