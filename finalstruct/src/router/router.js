import HelloWorld from '@/components/HelloWorld'
import userIndex from '@/components/UserIndex'
import item from '@/components/Item'
import itemstate from '@/components/ItemState'
import codewarehouse from '@/components/CodeWarehouse'
import codewarehousegit from '@/components/CodeWarehouseGit'
import codewarehousebranches from '@/components/CodeWarehouseBranches'
import codewarehouseversion from '@/components/CodeWarehouseVersion'
import codewarehouseversiondetail from '@/components/CodeWarehouseVersionDetail'
import codewarehousemerge from '@/components/CodeWarehouseMerge'
import codewarehousemergedetail from '@/components/CodeWarehouseMergeDetail'
import codewarehousemergecreate from '@/components/CodeWarehouseMergeCreate'
import betweengroup from '@/components/StatsBetweenGroup'
import intragroup from '@/components/StatsIntraGroup'
import itemlist from '@/components/ItemList'

export default [
  {
    path: '/user/:userID',
    name: 'user',
    props: true,
    component: userIndex,
    children: [
      {
        path: 'item/:itemID',
        name: 'item',
        props: true,
        component: item,
        redirect: {
          name: 'itemstate'
        },
        children: [
          {
            path: 'itemstate',
            name: 'itemstate',
            component: itemstate
          },
          {
            path: 'codewarehouse',
            name: 'codewarehouse',
            component: codewarehouse,
            redirect: {
              name: 'git'
            },
            children:[
              {
                path: 'git',
                name: 'git',
                component: codewarehousegit
              },
              {
                path: 'branches',
                name: 'branches',
                component: codewarehousebranches
              },
              {
                path: 'version',
                name: 'version',
                component: codewarehouseversion
              },
              {
                path: 'versiondetail',
                name: 'versiondetail',
                component: codewarehouseversiondetail
              },
              {
                path: 'merge',
                name: 'merge',
                component: codewarehousemerge
              },
              {
                path: 'mergedetail',
                name: 'mergedetail',
                component: codewarehousemergedetail
              },
              {
                path: 'mergecreate',
                name: 'mergecreate',
                component: codewarehousemergecreate
              }
            
            ]
          },
          {
            path: 'stats/betweengroup',
            name: 'betweengroup',
            component: betweengroup
          },
          {
            path:'stats/intragroup',
            name:'intragroup',
            component: intragroup
          }
        ]
      },
      {
        path: 'itemlist',
        name: 'itemlist',
        component: itemlist
      }
    ]
  },
  { 
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld,
  }
]