# 典型光储系统架构模板

本文档提供5种典型光储系统架构的完整 XML 模板，可直接用于 draw.io。

## 图片占位符说明

模板中使用以下占位符代表产品图片路径。使用时请替换为实际图片的 base64 数据（通过 `drawio-tool.py prepare` 生成）或实际文件路径。

| 占位符 | 产品 | 建议尺寸（宽×高） | 用途 |
|--------|------|-------------------|------|
| `{{IMAGE_MC_L430}}` | MC-L430 分体式储能柜 | 50×70 | 单台储能柜缩略图 |
| `{{IMAGE_WS_L4300}}` | WS-L4300 储能集装箱 | 250×90 | 集装箱全貌图 |

**使用方式：**
1. 用 `python3 drawio-tool.py prepare <图片路径> <宽> <高>` 生成 base64
2. 将模板中的 `{{IMAGE_MC_L430}}` 替换为 `data:image/png,<生成的base64>`（注意：**不要**加 `;base64`）
3. 或直接替换为图片的绝对路径（仅在 draw.io 编辑器中可用，CLI 导出会丢失）

## 模板列表

| # | 模板名称 | 适用场景 | 电压等级 |
|---|---------|---------|---------|
| 1 | 并网光储系统（分体式） | 方案A - 10×MC-L430 | 400V |
| 2 | 并网光储系统（集装箱式） | 方案B - WS-L4300 | 690V |
| 3 | 离网光储系统 | 无电网场景 | 400V |
| 4 | 微电网系统（并离网切换） | 并网/离网切换 | 400V |
| 5 | 工商业光储系统(C&I) | 几百kW项目 | 400V |
| 6 | 纯光伏系统（不带储能） | 仅光伏发电，无储能 | 400V |

---

## 模板1：并网光储系统（分体式）

**系统描述：** 基于Ketzin方案的完整分体式储能系统，使用10台MC-L430储能柜，总容量4.3MWh/2MW。

**系统特点：**
- 10台分体式储能柜 MC-L430（5×2排列）
- 4台STS静态转换开关
- 400V交流母线
- 升压变压器接入中压电网

### 完整 XML 模板

```xml
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="并网光储系统（分体式）&#xa;方案A：10×MC-L430储能柜" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="500" height="50" as="geometry"/>
    </mxCell>

    <!-- 光伏车棚 -->
    <mxCell id="pv_carport" value="光伏车棚系统&#xa;2 MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="400" y="90" width="180" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头：光伏到逆变器 -->
    <mxCell id="arrow_pv_inv" edge="1" parent="1" source="pv_carport" target="inverter">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 组串逆变器 -->
    <mxCell id="inverter" value="组串逆变器&#xa;(交流侧)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="420" y="170" width="140" height="40" as="geometry"/>
    </mxCell>

    <!-- 箭头：逆变器到交流母线 -->
    <mxCell id="arrow_inv_bus" edge="1" parent="1" source="inverter" target="ac_bus_container">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 交流母线容器 -->
    <mxCell id="ac_bus_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="120" y="240" width="760" height="320" as="geometry"/>
    </mxCell>

    <mxCell id="ac_bus_label" value="交流母线 400V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="130" y="245" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- 园区负载 -->
    <mxCell id="load" value="园区负载&#xa;峰值 ~918kW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="160" y="360" width="120" height="60" as="geometry"/>
    </mxCell>

    <!-- 储能系统容器 -->
    <mxCell id="ess_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2" vertex="1" parent="1">
      <mxGeometry x="340" y="270" width="500" height="270" as="geometry"/>
    </mxCell>

    <mxCell id="ess_label" value="储能系统 (4.3MWh / 2MW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#1A3D5C" vertex="1" parent="1">
      <mxGeometry x="460" y="275" width="200" height="25" as="geometry"/>
    </mxCell>

    <!-- MC-L430 储能柜 #1-5 第一排 -->
    <mxCell id="ess_img1" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="355" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label1" value="#1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="355" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img2" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="415" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label2" value="#2" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="415" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img3" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="475" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label3" value="#3" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="475" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img4" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="535" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label4" value="#4" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="535" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img5" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="595" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label5" value="#5" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="595" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <!-- MC-L430 储能柜 #6-10 第二排 -->
    <mxCell id="ess_img6" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="355" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label6" value="#6" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="355" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img7" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="415" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label7" value="#7" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="415" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img8" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="475" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label8" value="#8" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="475" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img9" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="535" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label9" value="#9" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="535" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img10" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="595" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label10" value="#10" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="595" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <!-- 型号标注 -->
    <mxCell id="ess_model" value="MC-L430-2H3 (430kWh/200kW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontStyle=2;fontColor=#6C8EBF" vertex="1" parent="1">
      <mxGeometry x="460" y="490" width="140" height="20" as="geometry"/>
    </mxCell>

    <!-- EMS控制器 -->
    <mxCell id="ems" value="EMS&#xa;MS-EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="670" y="400" width="60" height="40" as="geometry"/>
    </mxCell>

    <!-- STS切换柜 -->
    <mxCell id="sts1" value="STS&#xa;MS-TS500&#xa;×4" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="740" y="340" width="60" height="50" as="geometry"/>
    </mxCell>

    <!-- 变压器 -->
    <mxCell id="transformer" value="升压变压器&#xa;2,000 kVA&#xa;400V → 15kV/20kV" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="380" y="590" width="180" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：交流母线到变压器 -->
    <mxCell id="arrow_bus_trans" edge="1" parent="1" source="ac_bus_container" target="transformer">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 中压开关站 -->
    <mxCell id="mv_switch" value="中压开关站 (J08)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="680" width="140" height="40" as="geometry"/>
    </mxCell>

    <!-- 箭头：变压器到开关站 -->
    <mxCell id="arrow_trans_sw" edge="1" parent="1" source="transformer" target="mv_switch">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电网 -->
    <mxCell id="grid" value="E.DIS 电网&#xa;15kV / 20kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="740" width="140" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：开关站到电网 -->
    <mxCell id="arrow_sw_grid" edge="1" parent="1" source="mv_switch" target="grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

**布局说明：**
- 顶部：光伏车棚 → 组串逆变器
- 中部：交流母线容器内包含负载和储能系统
- 储能系统采用5×2排列的10台MC-L430
- EMS和STS在储能系统右侧
- 底部：变压器 → 中压开关 → 电网

---

## 模板2：并网光储系统（集装箱式）

**系统描述：** 基于Ketzin方案B的集装箱式储能系统，使用单台WS-L4300，总容量4.3MWh/2MW。

**系统特点：**
- 单台集装箱储能WS-L4300
- 2台STS静态转换开关
- 690V交流母线
- 升压变压器接入中压电网

### 完整 XML 模板

```xml
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="并网光储系统（集装箱式）&#xa;方案B：WS-L4300储能集装箱" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="500" height="50" as="geometry"/>
    </mxCell>

    <!-- 光伏车棚 -->
    <mxCell id="pv_carport" value="光伏车棚系统&#xa;2 MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="400" y="90" width="180" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头：光伏到逆变器 -->
    <mxCell id="arrow_pv_inv" edge="1" parent="1" source="pv_carport" target="inverter">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 组串逆变器 -->
    <mxCell id="inverter" value="组串逆变器&#xa;(交流侧)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="420" y="170" width="140" height="40" as="geometry"/>
    </mxCell>

    <!-- 箭头：逆变器到交流母线 -->
    <mxCell id="arrow_inv_bus" edge="1" parent="1" source="inverter" target="ac_bus_container">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 交流母线容器 -->
    <mxCell id="ac_bus_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="120" y="240" width="760" height="220" as="geometry"/>
    </mxCell>

    <mxCell id="ac_bus_label" value="交流母线 690V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="130" y="245" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- 园区负载 -->
    <mxCell id="load" value="园区负载&#xa;峰值 ~918kW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="160" y="310" width="120" height="60" as="geometry"/>
    </mxCell>

    <!-- WS-L4300 集装箱储能系统 -->
    <mxCell id="container_ess" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2" vertex="1" parent="1">
      <mxGeometry x="340" y="270" width="500" height="160" as="geometry"/>
    </mxCell>

    <mxCell id="container_ess_label" value="液冷储能集装箱 WS-L4300-BC-3 (4.3MWh / 2MW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#1A3D5C" vertex="1" parent="1">
      <mxGeometry x="420" y="275" width="340" height="25" as="geometry"/>
    </mxCell>

    <!-- WS-L4300 产品图片 -->
    <mxCell id="container_img" value="" style="image;image={{IMAGE_WS_L4300}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="360" y="305" width="280" height="100" as="geometry"/>
    </mxCell>

    <!-- EMS控制器 -->
    <mxCell id="ems" value="EMS&#xa;MS-EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="660" y="305" width="60" height="40" as="geometry"/>
    </mxCell>

    <!-- STS切换柜 -->
    <mxCell id="sts" value="STS&#xa;WS-TS1000&#xa;×2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="740" y="305" width="60" height="50" as="geometry"/>
    </mxCell>

    <!-- 内部组件标注 -->
    <mxCell id="container_note" value="集成: 电池 + PCS + BMS + 消防 + 空调" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontStyle=2;fontColor=#6C8EBF" vertex="1" parent="1">
      <mxGeometry x="420" y="405" width="200" height="20" as="geometry"/>
    </mxCell>

    <!-- 警告标注 -->
    <mxCell id="warning" value="注意: 690V输出需确认变压器兼容性" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#CC0000;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="560" y="480" width="220" height="20" as="geometry"/>
    </mxCell>

    <!-- 变压器 -->
    <mxCell id="transformer" value="升压变压器&#xa;2,000 kVA&#xa;690V → 15kV/20kV" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="380" y="510" width="180" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：交流母线到变压器 -->
    <mxCell id="arrow_bus_trans" edge="1" parent="1" source="ac_bus_container" target="transformer">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 中压开关站 -->
    <mxCell id="mv_switch" value="中压开关站 (J08)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="600" width="140" height="40" as="geometry"/>
    </mxCell>

    <!-- 箭头：变压器到开关站 -->
    <mxCell id="arrow_trans_sw" edge="1" parent="1" source="transformer" target="mv_switch">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电网 -->
    <mxCell id="grid" value="E.DIS 电网&#xa;15kV / 20kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="660" width="140" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：开关站到电网 -->
    <mxCell id="arrow_sw_grid" edge="1" parent="1" source="mv_switch" target="grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

**布局说明：**
- 顶部：光伏车棚 → 组串逆变器
- 中部：交流母线容器内包含负载和集装箱ESS
- 集装箱内集成电池、PCS、BMS、消防、空调
- EMS和STS在集装箱右侧
- 底部：变压器（690V）→ 中压开关 → 电网
- 关键提醒：690V输出需确认变压器兼容性

---

## 模板3：离网光储系统

**系统描述：** 离网型光储系统，无电网接入，适用于偏远地区或岛屿。

**系统特点：**
- 光伏 + 储能 + 柴油发电机
- 无电网接入
- 400V交流母线
- 柴发作为备用电源

### 完整 XML 模板

```xml
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="离网光储系统&#xa;光伏 + 储能 + 柴油发电机" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="500" height="50" as="geometry"/>
    </mxCell>

    <!-- 光伏组件 -->
    <mxCell id="pv_array" value="光伏组件&#xa;2 MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="400" y="90" width="180" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头：光伏到逆变器 -->
    <mxCell id="arrow_pv_inv" edge="1" parent="1" source="pv_array" target="inverter">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 组串逆变器 -->
    <mxCell id="inverter" value="组串逆变器&#xa;(交流侧)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="420" y="170" width="140" height="40" as="geometry"/>
    </mxCell>

    <!-- 箭头：逆变器到交流母线 -->
    <mxCell id="arrow_inv_bus" edge="1" parent="1" source="inverter" target="ac_bus_container">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 交流母线容器 -->
    <mxCell id="ac_bus_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="120" y="240" width="760" height="280" as="geometry"/>
    </mxCell>

    <mxCell id="ac_bus_label" value="交流母线 400V (离网)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="130" y="245" width="120" height="20" as="geometry"/>
    </mxCell>

    <!-- 负载 -->
    <mxCell id="load" value="园区负载&#xa;峰值 ~918kW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="160" y="360" width="120" height="60" as="geometry"/>
    </mxCell>

    <!-- 储能系统容器 -->
    <mxCell id="ess_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2" vertex="1" parent="1">
      <mxGeometry x="340" y="270" width="500" height="220" as="geometry"/>
    </mxCell>

    <mxCell id="ess_label" value="储能系统 (4.3MWh / 2MW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#1A3D5C" vertex="1" parent="1">
      <mxGeometry x="460" y="275" width="200" height="25" as="geometry"/>
    </mxCell>

    <!-- MC-L430 储能柜 #1-5 第一排 -->
    <mxCell id="ess_img1" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="355" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label1" value="#1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="355" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img2" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="415" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label2" value="#2" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="415" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img3" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="475" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label3" value="#3" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="475" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img4" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="535" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label4" value="#4" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="535" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img5" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="595" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label5" value="#5" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="595" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <!-- MC-L430 储能柜 #6-10 第二排 -->
    <mxCell id="ess_img6" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="355" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label6" value="#6" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="355" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img7" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="415" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label7" value="#7" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="415" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img8" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="475" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label8" value="#8" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="475" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img9" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="535" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label9" value="#9" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="535" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img10" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="595" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label10" value="#10" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="595" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <!-- 型号标注 -->
    <mxCell id="ess_model" value="MC-L430-2H3 (430kWh/200kW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontStyle=2;fontColor=#6C8EBF" vertex="1" parent="1">
      <mxGeometry x="460" y="490" width="140" height="20" as="geometry"/>
    </mxCell>

    <!-- EMS控制器 -->
    <mxCell id="ems" value="EMS&#xa;MS-EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="670" y="350" width="60" height="40" as="geometry"/>
    </mxCell>

    <!-- 柴油发电机 -->
    <mxCell id="diesel_gen" value="柴油发电机&#xa;Backup&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="740" y="350" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- 无电网标注 -->
    <mxCell id="no_grid_note" value="无电网接入 (离网系统)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontColor=#CC0000;fontStyle=2" vertex="1" parent="1">
      <mxGeometry x="380" y="550" width="180" height="30" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

**布局说明：**
- 顶部：光伏组件 → 组串逆变器
- 中部：交流母线容器内包含负载和储能系统
- 与并网系统的主要区别：无变压器、无中压开关、无电网
- 柴油发电机作为离网备用电源
- EMS负责离网运行的能量管理

---

## 模板4：微电网系统（并离网切换）

**系统描述：** 支持并网和离网模式切换的微电网系统，包含STS静态转换开关。

**系统特点：**
- 光伏 + 储能 + 电网 + 柴油发电机
- STS静态转换开关实现无缝切换
- 400V交流母线
- 多能源协调控制

### 完整 XML 模板

```xml
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="微电网系统（并离网切换）&#xa;含STS无缝切换" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="500" height="50" as="geometry"/>
    </mxCell>

    <!-- 光伏车棚 -->
    <mxCell id="pv_carport" value="光伏车棚&#xa;2 MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="400" y="90" width="180" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头：光伏到逆变器 -->
    <mxCell id="arrow_pv_inv" edge="1" parent="1" source="pv_carport" target="inverter">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 组串逆变器 -->
    <mxCell id="inverter" value="组串逆变器&#xa;(交流侧)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="420" y="170" width="140" height="40" as="geometry"/>
    </mxCell>

    <!-- 箭头：逆变器到交流母线 -->
    <mxCell id="arrow_inv_bus" edge="1" parent="1" source="inverter" target="ac_bus_container">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 交流母线容器 -->
    <mxCell id="ac_bus_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="120" y="240" width="760" height="350" as="geometry"/>
    </mxCell>

    <mxCell id="ac_bus_label" value="交流母线 400V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="130" y="245" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- 园区负载 -->
    <mxCell id="load" value="园区负载&#xa;峰值 ~918kW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="160" y="360" width="120" height="60" as="geometry"/>
    </mxCell>

    <!-- 储能系统容器 -->
    <mxCell id="ess_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2" vertex="1" parent="1">
      <mxGeometry x="340" y="270" width="500" height="290" as="geometry"/>
    </mxCell>

    <mxCell id="ess_label" value="储能系统 (4.3MWh / 2MW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#1A3D5C" vertex="1" parent="1">
      <mxGeometry x="460" y="275" width="200" height="25" as="geometry"/>
    </mxCell>

    <!-- MC-L430 储能柜 #1-5 第一排 -->
    <mxCell id="ess_img1" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="355" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label1" value="#1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="355" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img2" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="415" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label2" value="#2" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="415" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img3" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="475" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label3" value="#3" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="475" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img4" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="535" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label4" value="#4" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="535" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img5" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="595" y="305" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label5" value="#5" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="595" y="375" width="50" height="15" as="geometry"/>
    </mxCell>

    <!-- MC-L430 储能柜 #6-10 第二排 -->
    <mxCell id="ess_img6" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="355" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label6" value="#6" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="355" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img7" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="415" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label7" value="#7" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="415" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img8" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="475" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label8" value="#8" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="475" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img9" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="535" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label9" value="#9" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="535" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <mxCell id="ess_img10" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="595" y="400" width="50" height="70" as="geometry"/>
    </mxCell>
    <mxCell id="ess_label10" value="#10" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="595" y="470" width="50" height="15" as="geometry"/>
    </mxCell>

    <!-- EMS控制器 -->
    <mxCell id="ems" value="EMS&#xa;MS-EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="670" y="350" width="60" height="40" as="geometry"/>
    </mxCell>

    <!-- STS切换柜 -->
    <mxCell id="sts1" value="STS&#xa;MS-TS500&#xa;×4" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="740" y="290" width="60" height="50" as="geometry"/>
    </mxCell>

    <!-- 柴油发电机 -->
    <mxCell id="diesel_gen" value="柴发&#xa;Backup&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="740" y="420" width="80" height="60" as="geometry"/>
    </mxCell>

    <!-- 变压器 -->
    <mxCell id="transformer" value="升压变压器&#xa;2,000 kVA" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="380" y="620" width="180" height="60" as="geometry"/>
    </mxCell>

    <!-- STS切换逻辑标注 -->
    <mxCell id="sts_note" value="STS: 并网/离网&#xa;无缝切换" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#D79B00;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="130" y="520" width="100" height="40" as="geometry"/>
    </mxCell>

    <!-- 中压开关站 -->
    <mxCell id="mv_switch" value="中压开关站 (J08)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="710" width="140" height="40" as="geometry"/>
    </mxCell>

    <!-- 电网 -->
    <mxCell id="grid" value="电网&#xa;15kV / 20kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="770" width="140" height="60" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

**布局说明：**
- 顶部：光伏车棚 → 组串逆变器
- 中部：交流母线容器内包含负载、储能系统、STS、柴发
- STS位于储能系统和电网之间，实现无缝切换
- 柴发作为离网模式的备用电源
- 底部：变压器 → 中压开关 → 电网

---

## 模板5：工商业光储系统（C&I）

**系统描述：** 适用于工商业用户的较小规模光储系统（几百kW），典型的AC Coupling结构。

**系统特点：**
- 规模较小（200kW/400kWh）
- 400V低压并网
- AC Coupling交流耦合
- 适合C&I场景

### 完整 XML 模板

```xml
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="工商业光储系统 (C&I)&#xa;AC Coupling 结构" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="500" height="50" as="geometry"/>
    </mxCell>

    <!-- 光伏组件 -->
    <mxCell id="pv_array" value="光伏组件&#xa;200 kWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="120" y="100" width="140" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头：光伏到逆变器 -->
    <mxCell id="arrow_pv_inv" edge="1" parent="1" source="pv_array" target="pv_inverter">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 光伏逆变器 -->
    <mxCell id="pv_inverter" value="光伏逆变器&#xa;200kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="120" y="180" width="140" height="50" as="geometry"/>
    </mxCell>

    <!-- 交流母线容器 -->
    <mxCell id="ac_bus_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="80" y="260" width="640" height="200" as="geometry"/>
    </mxCell>

    <mxCell id="ac_bus_label" value="交流母线 400V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="90" y="265" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- 商业负载 -->
    <mxCell id="load" value="商业负载&#xa;峰值 150kW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="100" y="360" width="120" height="60" as="geometry"/>
    </mxCell>

    <!-- PCS双向变流器 -->
    <mxCell id="pcs" value="PCS&#xa;100kW&#xa;双向变流器" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="280" y="300" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- 电池簇 -->
    <mxCell id="battery" value="电池簇&#xa;400kWh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="280" y="380" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- EMS控制器 -->
    <mxCell id="ems" value="EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="420" y="300" width="60" height="40" as="geometry"/>
    </mxCell>

    <!-- STS切换柜 -->
    <mxCell id="sts" value="STS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="420" y="360" width="60" height="40" as="geometry"/>
    </mxCell>

    <!-- 变压器 -->
    <mxCell id="transformer" value="变压器&#xa;250 kVA" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="540" y="300" width="140" height="60" as="geometry"/>
    </mxCell>

    <!-- 电网 -->
    <mxCell id="grid" value="电网&#xa;400V" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="540" y="400" width="140" height="50" as="geometry"/>
    </mxCell>

    <!-- 连接线 -->
    <mxCell id="arrow_bus_pcs" edge="1" parent="1" source="ac_bus_container" target="pcs">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <mxCell id="arrow_bus_trans" edge="1" parent="1" source="ac_bus_container" target="transformer">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <mxCell id="arrow_trans_grid" edge="1" parent="1" source="transformer" target="grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 系统参数标注 -->
    <mxCell id="sys_note" value="系统容量: 200kWp光伏 + 400kWh/100kW储能" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="240" y="480" width="240" height="20" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

**布局说明：**
- 左侧：光伏组件 → 光伏逆变器
- 中部：交流母线容器内包含负载、PCS电池簇、EMS、STS
- 右侧：变压器 → 电网
- C&I系统规模较小，结构简洁
- AC Coupling结构：光伏和储能都通过AC母线接入

---

## 模板6：纯光伏系统（不带储能）

**系统描述：** 纯光伏发电系统，不含储能设备。适用于白天发电即用场景。

**系统特点：**
- 光伏组件 + 组串逆变器
- 无储能系统
- 400V低压并网
- 适用于自发自用场景

### 完整 XML 模板

```xml
<mxGraphModel adaptiveColors="auto">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="纯光伏系统（不带储能）&#xa;自发自用方案" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=16;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="50" as="geometry"/>
    </mxCell>

    <!-- 光伏组件阵列 -->
    <mxCell id="pv_array" value="光伏组件阵列&#xa;2 MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="100" y="100" width="200" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：光伏到逆变器 -->
    <mxCell id="arrow_pv_inv" edge="1" parent="1" source="pv_array" target="pv_inverter">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 组串逆变器 -->
    <mxCell id="pv_inverter" value="组串逆变器&#xa;PV Inverter" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="420" y="100" width="140" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：逆变器到变压器 -->
    <mxCell id="arrow_inv_xfmr" edge="1" parent="1" source="pv_inverter" target="transformer">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 升压变压器 -->
    <mxCell id="transformer" value="升压变压器&#xa;400V→10kV" style="shape=hexagon;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="620" y="90" width="120" height="80" as="geometry"/>
    </mxCell>

    <!-- 箭头：变压器到电网 -->
    <mxCell id="arrow_xfmr_grid" edge="1" parent="1" source="transformer" target="grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电网接入点 -->
    <mxCell id="grid" value="电网&#xa;10kV" style="shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="800" y="90" width="100" height="80" as="geometry"/>
    </mxCell>

    <!-- 交流母线容器 -->
    <mxCell id="ac_bus_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="50" y="200" width="700" height="120" as="geometry"/>
    </mxCell>

    <mxCell id="ac_bus_label" value="交流母线 400V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="60" y="205" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- 负载 -->
    <mxCell id="load" value="园区负载&#xa;1.5 MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
      <mxGeometry x="350" y="230" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：母线到负载 -->
    <mxCell id="arrow_bus_load" edge="1" parent="1" source="ac_bus_container" target="load">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 计量箱 -->
    <mxCell id="meter" value="双向电度表" style="shape=required;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="550" y="240" width="80" height="40" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

**布局说明：**
- 顶部：光伏组件 → 逆变器 → 变压器 → 电网
- 中部：交流母线容器
- 底部：园区负载
- 无储能设备
- 简洁的单向功率流

---

## 使用说明

1. **复制XML**：将所需模板的完整 XML 代码复制到剪贴板
2. **创建文件**：在 draw.io 中新建文件或创建 .drawio 文本文件
3. **导入XML**：在 draw.io 中使用 File > Open 导入 XML，或直接替换文件内容
4. **自定义修改**：
   - 修改组件参数（容量、数量）
   - 调整布局位置
   - 添加或删除组件
5. **导出格式**：支持 PNG、SVG、PDF 导出
