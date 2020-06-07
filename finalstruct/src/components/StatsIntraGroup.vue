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
    <Split v-model="split1">
      <div slot="left">
        <div id="myChart" style="width:800px;height:650px"></div>
      </div>
      <div slot="right">
        <Card :bordered="false">
          <p slot="title">评分依据</p>
          Com1=-0.452cmt*-0.437add*-0.454del*-0.441fixes*-0.452files*
          Com1=-0.493comments*-0.502pr*-0.51issues*-0.494handle_issues*
          Com2=0.535comments*-0.576pr*-0.404issues*0.468handle_issues*
          Com=17.437Com1+1.282Com2
        </Card>
        <Table border :columns="columns" :data="countdata" width=447></Table>
      </div>
    </Split>
  </div>
</template>
<script>
export default {
  data() {
    return {
      split1: 0.66,
      columns: [
        {
          title: "姓名",
          key: "name"
        },
        {
          title: "评分",
          key: "countdata",
          sortable: true
        }
      ],
      countdata:[]
    };
  },
  mounted() {
    this.drawLine();
  },
  methods: {
    drawLine() {
      var temp;
      this.$http
        .get(
          "/static/finalstruct/project_" + this.$route.params.itemID + ".json"
        )
        .then(res => {
          // console.log(res);
          // this.data=res.body.RECORDS;
          temp = JSON.parse(JSON.stringify(res.body.RECORDS));
          var project_data = [];
          var name_data = [];
          var index = 0;
          for (index; index < temp.length; index++) {
            var temp_data = {
              name: temp[index].name,
              value: [
                temp[index].cmt,
                temp[index].add,
                temp[index].del,
                temp[index].fixes,
                temp[index].files,
                temp[index].issues,
                temp[index].handle_issues,
                temp[index].pr,
                temp[index].comments
              ]
            };
            project_data.push(temp_data);
            name_data.push(temp[index].name);
            var count_data_temp=0.504*temp[index].add+0.159*temp[index].del+0.016*temp[index].fixes+1.662*temp[index].files+0.099*temp[index].issues;+0.012*temp[index].handle_issues+0.024*temp[index].pr+0.087*temp[index].comments;
            var count_data = {
              name: temp[index].name,
              countdata: count_data_temp.toFixed(2)
            };
            this.countdata.push(count_data);
          }
          var Option = {
            title: {
              text: "贡献者能力雷达图(已标准化1-10）"
            },
            tooltip: {},
            legend: {
              bottom: 5,
              data: name_data
              // selectedMode: "single"
            },
            radar: {
              // shape: 'circle',
              name: {
                textStyle: {
                  color: "#fff",
                  backgroundColor: "#999",
                  borderRadius: 3,
                  padding: [3, 5]
                }
              },
              indicator: [
                { name: "提交代码次数(cmt)", max: 10 },
                { name: "增加代码行数(add)", max: 10 },
                { name: "删除代码行数(del)", max: 10 },
                { name: "修复bug数量(fixes)", max: 10 },
                { name: "维护或修改文件的数量(files)", max: 10 },
                { name: "发布问题跟踪数量(issues)", max: 10 },
                { name: "完成问题跟踪数量(handle_issues)", max: 10 },
                { name: "发起请求代码合并次数(pr)", max: 10 },
                { name: "评论次数(comments)", max: 10 }
              ]
            },
            series: [
              {
                name: "个人能力雷达图",
                type: "radar",
                // areaStyle: {normal: {}},
                data: project_data
              }
            ]
          };
          console.log(Option);
          // 基于准备好的dom，初始化echarts实例
          let myChart = this.$echarts.init(document.getElementById("myChart"));

          myChart.setOption(Option);
        })
        .catch(err => {
          console.error(err);
        });
    }
  },
  beforeCreate() {
    //   this.$http
    //     .get("/static/finalstruct/project_" + this.$route.params.itemID + ".json")
    //     .then(res => {
    //       // var obj = JSON.parse(res.RECORDS);
    //       console.log(res.body.RECORDS);
    //       this.data=res.body.RECORDS;
    //       console.log(this.data[0].cmt);
    //     })
    //     .catch(err => {
    //       console.error(err);
    //     });
  }
};
</script>