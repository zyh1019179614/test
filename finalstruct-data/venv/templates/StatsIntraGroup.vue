<style scoped>
.content {
  background-color: white;
  height: 200vh;
  overflow-y: hidden;
  overflow-x: hidden;
  width: 100%;
}
</style>
<template>
<div class="content">
    贡献者能力雷达图
    贡献演化年轮图
    贡献演化平行坐标线性图
    代码的质量分析数据
    <div id="myChart" :style="{width: '300px', height: '300px'}"></div>
</div>
</template>
<script>
export default {
  data () {
    return {
    }
  },
  mounted(){
    this.drawLine();
  },
  methods: {
    drawLine(){
        // 基于准备好的dom，初始化echarts实例
        let myChart = this.$echarts.init(document.getElementById('myChart'))
        // 绘制图表
        myChart.setOption({
            title: { text: '在Vue中使用echarts' },
            tooltip: {},
            xAxis: {
                data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        });
    }
  }
}
</script>