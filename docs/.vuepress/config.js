module.exports = {

//针对不同项目，需要修改的参数有：base,title,description,repo以及nav,sidebar 文件夹下的导航js文件

base: '/docs/linux/',
dest: 'html/linux',

head: [
  ['link', { rel: 'icon', href: '/favcon.ico' }]
],

//vuepress多语言，区别于主题多语言
locales: {
    '/': {
      lang: 'en-US', // 将会被设置为 <html> 的 lang 属性
      title: 'Linux Guide',
      description: 'This document is a summary of Linux-related operations, commands, and scripts in Websoft9 to help cloud computing users quickly master Linux-related skills.'
    },
    '/zh/': {
      lang: 'zh-CN',
      title: 'Linux 实践指南',
      description: '本文档是Websoft9在实践中，总结的与Linux有关的操作、命令、脚本，帮助云计算用户快速掌握Linux相关的技能'
    }
},

themeConfig: {
	 
	//Basic configuration
	displayAllHeaders: false, // 默认值：false
  activeHeaderLinks: true, // 默认值：true
  displayAllHeaders: false, // 默认值：false
  sidebar: 'auto', // 默认值：false
  sidebarDepth: 2,

  //Github 
  repo: 'Websoft9/linux',
  editLinks: true,
  docsDir: 'docs',
  docsBranch: 'main',

  //主题多语言
  locales: {
    '/': {
      label: 'English',
      selectText: 'Languages',
      editLinkText: 'Edit this page on GitHub',
      lastUpdated: 'Last Updated',
      serviceWorker: {
         updatePopup: {
         message: "New content is available.",
         buttonText: "Refresh"
          }
        },
  
    //top-menu
    nav: require('./nav/en'),
    //left-menu
    sidebar:require('./sidebar/en'),
  },  
  
  '/zh/': {
    label: '中文',
    selectText: '语言',
    editLinkText: '在Github上编辑',
    lastUpdated: 'Last Updated',
    serviceWorker: {
      updatePopup: {
        message: "此文档有可用的更新",
        buttonText: "刷新"
      }
    },
  
    //页眉
    nav: require('./nav/zh'),
    //侧边栏导航
    sidebar: require('./sidebar/zh'),
  
  },
  
},   
}
}