# 电气单线图模板

本文档提供6种电气单线图模板，适用于不同电压等级和应用场景。

## 模板列表

| # | 模板名称 | 适用场景 | 电压等级 |
|---|---------|---------|---------|
| 1 | 低压并网单线图 | C&I项目 | 400V |
| 2 | 中压并网单线图 | 集装箱ESS项目 | 690V |
| 3 | 高压并网单线图 | 大型地面电站 | 10kV/20kV |
| 4 | 电池簇直流单线图 | BMS和电池簇详情 | 直流侧 |
| 5 | 并离网切换单线图 | STS切换逻辑 | 400V |
| 6 | 微电网单线图 | 多能源接入 | 400V |

---

## 模板1：低压并网单线图（400V）

**适用场景：** 典型的工商业（C&I）项目，400V低压并网。

**特点：**
- 400V低压侧接线
- 单台变压器
- 简单并网结构

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="低压并网单线图 (400V)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- 光伏组件 -->
    <mxCell id="pv" value="光伏阵列&#xa;200kWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="40" y="120" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 光伏逆变器 -->
    <mxCell id="pv_inv" value="光伏逆变器&#xa;AC 200kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="160" y="120" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 直流电缆 -->
    <mxCell id="dc_line1" value="DC" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8" vertex="1" parent="1">
      <mxGeometry x="125" y="90" width="30" height="20" as="geometry"/>
    </mxCell>

    <!-- 箭头线：光伏到逆变器 -->
    <mxCell id="arrow1" edge="1" parent="1" source="pv" target="pv_inv">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 400V母线 -->
    <mxCell id="bus_400v" value="400V AC" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="280" y="100" width="20" height="90" as="geometry"/>
    </mxCell>

    <!-- 箭头线：逆变器到母线 -->
    <mxCell id="arrow2" edge="1" parent="1" source="pv_inv" target="bus_400v">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- PCS变流器 -->
    <mxCell id="pcs" value="PCS&#xa;双向100kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="340" y="120" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头线：PCS到母线 -->
    <mxCell id="arrow3" edge="1" parent="1" source="pcs" target="bus_400v">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电池簇 -->
    <mxCell id="battery" value="电池簇&#xa;400kWh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="340" y="200" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 直流电缆标注 -->
    <mxCell id="dc_line2" value="DC" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8" vertex="1" parent="1">
      <mxGeometry x="375" y="175" width="30" height="20" as="geometry"/>
    </mxCell>

    <!-- 箭头线：PCS到电池 -->
    <mxCell id="arrow4" edge="1" parent="1" source="pcs" target="battery">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 负载 -->
    <mxCell id="load" value="负载&#xa;150kW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="120" width="70" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头线：母线到负载 -->
    <mxCell id="arrow5" edge="1" parent="1" source="bus_400v" target="load">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 变压器 -->
    <mxCell id="transformer" value="变压器&#xa;250kVA" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="460" y="200" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头线：母线到变压器 -->
    <mxCell id="arrow6" edge="1" parent="1" source="bus_400v" target="transformer">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电网侧 -->
    <mxCell id="grid" value="电网&#xa;400V" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="570" y="200" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头线：变压器到电网 -->
    <mxCell id="arrow7" edge="1" parent="1" source="transformer" target="grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- EMS -->
    <mxCell id="ems" value="EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="340" y="280" width="50" height="30" as="geometry"/>
    </mxCell>

    <!-- EMS连接线 -->
    <mxCell id="arrow8" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" parent="1" source="battery" target="ems">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板2：中压并网单线图（690V）

**适用场景：** 集装箱ESS项目，690V中压侧接线。

**特点：**
- 690V中压侧接线
- 适合WS-L4300集装箱
- 升压变压器

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="中压并网单线图 (690V)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- 光伏组件 -->
    <mxCell id="pv" value="光伏阵列&#xa;2MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="40" y="100" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 组串逆变器 -->
    <mxCell id="pv_inv" value="组串逆变器&#xa;AC 2MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="160" y="100" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头线 -->
    <mxCell id="arrow1" edge="1" parent="1" source="pv" target="pv_inv">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 690V母线 -->
    <mxCell id="bus_690v" value="690V AC" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10;verticalAlign=top;" vertex="1" parent="1">
      <mxGeometry x="280" y="80" width="20" height="120" as="geometry"/>
    </mxCell>

    <!-- 箭头线：逆变器到母线 -->
    <mxCell id="arrow2" edge="1" parent="1" source="pv_inv" target="bus_690v">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- WS-L4300集装箱 -->
    <mxCell id="ess" value="WS-L4300-BC-3&#xa;4.3MWh/2MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="340" y="100" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头线：ESS到母线 -->
    <mxCell id="arrow3" edge="1" parent="1" source="ess" target="bus_690v">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- STS -->
    <mxCell id="sts" value="STS&#xa;×2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="480" y="100" width="60" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头线：STS到母线 -->
    <mxCell id="arrow4" edge="1" parent="1" source="bus_690v" target="sts">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 变压器 -->
    <mxCell id="transformer" value="升压变压器&#xa;2000kVA&#xa;690V→20kV" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="580" y="90" width="100" height="70" as="geometry"/>
    </mxCell>

    <!-- 箭头线：STS到变压器 -->
    <mxCell id="arrow5" edge="1" parent="1" source="sts" target="transformer">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 中压开关 -->
    <mxCell id="mv_switch" value="MV Switchgear&#xa;20kV" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="580" y="200" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头线：变压器到开关 -->
    <mxCell id="arrow6" edge="1" parent="1" source="transformer" target="mv_switch">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电网 -->
    <mxCell id="grid" value="电网&#xa;20kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="580" y="290" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头线：开关到电网 -->
    <mxCell id="arrow7" edge="1" parent="1" source="mv_switch" target="grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- EMS -->
    <mxCell id="ems" value="EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="340" y="190" width="50" height="30" as="geometry"/>
    </mxCell>

    <!-- EMS连接 -->
    <mxCell id="arrow8" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" parent="1" source="ess" target="ems">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 警告标注 -->
    <mxCell id="warning" value="注意: 690V输出需确认变压器兼容性" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#CC0000" vertex="1" parent="1">
      <mxGeometry x="340" y="260" width="200" height="20" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板3：高压并网单线图（10kV/20kV）

**适用场景：** 大型地面电站，10kV或20kV高压并网。

**特点：**
- 10kV/20kV高压侧接线
- 主变压器和升压变压器
- 电网接入点

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="高压并网单线图 (10kV/20kV)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- 光伏组件阵列 -->
    <mxCell id="pv" value="光伏组件阵列&#xa;10MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="40" y="100" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- 箱式逆变器 -->
    <mxCell id="pv_inv" value="箱式逆变器&#xa;AC 10MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="180" y="100" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头 -->
    <mxCell id="arrow1" edge="1" parent="1" source="pv" target="pv_inv">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 10kV母线 -->
    <mxCell id="bus_10kv" value="10kV" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=12;verticalAlign=top;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="320" y="80" width="20" height="100" as="geometry"/>
    </mxCell>

    <!-- 箭头：逆变器到母线 -->
    <mxCell id="arrow2" edge="1" parent="1" source="pv_inv" target="bus_10kv">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- ESS储能系统 -->
    <mxCell id="ess" value="ESS储能系统&#xa;20MWh/5MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="380" y="90" width="120" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：ESS到母线 -->
    <mxCell id="arrow3" edge="1" parent="1" source="ess" target="bus_10kv">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 主变压器 -->
    <mxCell id="main_trafo" value="主变压器&#xa;12.5MVA&#xa;10kV/110kV" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="540" y="70" width="120" height="80" as="geometry"/>
    </mxCell>

    <!-- 箭头：母线到变压器 -->
    <mxCell id="arrow4" edge="1" parent="1" source="bus_10kv" target="main_trafo">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 高压开关 -->
    <mxCell id="hv_switch" value="GIS/HV Switchgear&#xa;110kV" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="540" y="200" width="120" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头 -->
    <mxCell id="arrow5" edge="1" parent="1" source="main_trafo" target="hv_switch">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电网接入点 -->
    <mxCell id="grid" value="电网&#xa;110kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="540" y="300" width="120" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头 -->
    <mxCell id="arrow6" edge="1" parent="1" source="hv_switch" target="grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- EMS -->
    <mxCell id="ems" value="EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="380" y="180" width="50" height="30" as="geometry"/>
    </mxCell>

    <!-- EMS连接 -->
    <mxCell id="arrow7" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" parent="1" source="ess" target="ems">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 功率标注 -->
    <mxCell id="power_note" value="Pmax = 10MW&#xa;卖电阈值" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="40" y="160" width="80" height="30" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板4：电池簇直流单线图

**适用场景：** 展示BMS和电池簇的直流侧接线详情。

**特点：**
- 直流侧详细接线
- BMS系统架构
- 电池簇级联

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="电池簇直流单线图" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- PCS直流侧 -->
    <mxCell id="pcs_dc" value="PCS&#xa;直流侧" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="320" y="80" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 直流母线 -->
    <mxCell id="dc_bus" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#9673A6;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="180" y="100" width="360" height="150" as="geometry"/>
    </mxCell>

    <mxCell id="dc_bus_label" value="直流母线 1500V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#9673A6" vertex="1" parent="1">
      <mxGeometry x="190" y="105" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- 电池簇1 -->
    <mxCell id="cluster1" value="电池簇 #1&#xa;100kWh/50kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="200" y="140" width="80" height="60" as="geometry"/>
    </mxCell>

    <!-- 电池簇2 -->
    <mxCell id="cluster2" value="电池簇 #2&#xa;100kWh/50kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="300" y="140" width="80" height="60" as="geometry"/>
    </mxCell>

    <!-- 电池簇3 -->
    <mxCell id="cluster3" value="电池簇 #3&#xa;100kWh/50kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="400" y="140" width="80" height="60" as="geometry"/>
    </mxCell>

    <!-- 电池簇4 -->
    <mxCell id="cluster4" value="电池簇 #4&#xa;100kWh/50kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="500" y="140" width="80" height="60" as="geometry"/>
    </mxCell>

    <!-- 连接线：电池簇到直流母线 -->
    <mxCell id="arrow1" edge="1" parent="1" source="cluster1" target="dc_bus">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="arrow2" edge="1" parent="1" source="cluster2" target="dc_bus">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="arrow3" edge="1" parent="1" source="cluster3" target="dc_bus">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="arrow4" edge="1" parent="1" source="cluster4" target="dc_bus">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 直流母线到PCS -->
    <mxCell id="arrow5" edge="1" parent="1" source="dc_bus" target="pcs_dc">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- BMS系统 -->
    <mxCell id="bms" value="BMS&#xa;电池管理系统" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="320" y="280" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- BMS连接线 -->
    <mxCell id="bms_arrow1" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" parent="1" source="cluster1" target="bms">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="bms_arrow2" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" parent="1" source="cluster2" target="bms">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="bms_arrow3" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" parent="1" source="cluster3" target="bms">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>
    <mxCell id="bms_arrow4" style="edgeStyle=orthogonalEdgeStyle;dashed=1;" edge="1" parent="1" source="cluster4" target="bms">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电池模组详情 -->
    <mxCell id="module_detail" value="每簇包含: 电池模组×14 (3.57kWh/模组)&#xa;Pack×4 (50kWh/Pack)" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="40" y="380" width="250" height="30" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板5：并离网切换单线图

**适用场景：** 包含STS静态转换开关的并网/离网切换系统。

**特点：**
- STS双电源切换
- 并网/离网模式切换
- 无缝切换逻辑

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="并离网切换单线图 (STS)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- 光伏组件 -->
    <mxCell id="pv" value="光伏阵列&#xa;2MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="40" y="100" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 组串逆变器 -->
    <mxCell id="pv_inv" value="组串逆变器&#xa;AC 2MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="160" y="100" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头 -->
    <mxCell id="arrow1" edge="1" parent="1" source="pv" target="pv_inv">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 交流母线 -->
    <mxCell id="ac_bus" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="280" y="80" width="200" height="160" as="geometry"/>
    </mxCell>

    <mxCell id="ac_bus_label" value="交流母线 400V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="290" y="85" width="100" height="20" as="geometry"/>
    </mxCell>

    <!-- 箭头：逆变器到母线 -->
    <mxCell id="arrow2" edge="1" parent="1" source="pv_inv" target="ac_bus">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 储能PCS -->
    <mxCell id="pcs" value="PCS&#xa;2MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="300" y="100" width="70" height="50" as="geometry"/>
    </mxCell>

    <!-- 电池簇 -->
    <mxCell id="battery" value="电池簇&#xa;4.3MWh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="300" y="160" width="70" height="50" as="geometry"/>
    </mxCell>

    <!-- EMS -->
    <mxCell id="ems" value="EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="390" y="100" width="50" height="30" as="geometry"/>
    </mxCell>

    <!-- 柴油发电机 -->
    <mxCell id="diesel" value="柴发&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="390" y="160" width="70" height="50" as="geometry"/>
    </mxCell>

    <!-- STS切换开关 -->
    <mxCell id="sts" value="STS&#xa;静态转换开关" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="320" y="280" width="120" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头：母线到STS -->
    <mxCell id="arrow3" edge="1" parent="1" source="ac_bus" target="sts">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 变压器 -->
    <mxCell id="transformer" value="变压器&#xa;2000kVA" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="500" y="270" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：STS到变压器 -->
    <mxCell id="arrow4" edge="1" parent="1" source="sts" target="transformer">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 电网 -->
    <mxCell id="grid" value="电网&#xa;15kV/20kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="500" y="360" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头：变压器到电网 -->
    <mxCell id="arrow5" edge="1" parent="1" source="transformer" target="grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 切换模式标注 -->
    <mxCell id="mode_note" value="并网模式: 电网供电&#xa;离网模式: 柴发+储能" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#D79B00" vertex="1" parent="1">
      <mxGeometry x="40" y="200" width="120" height="40" as="geometry"/>
    </mxCell>

    <!-- 切换逻辑 -->
    <mxCell id="switch_logic" value="STS: &lt;20ms 无缝切换" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontColor=#CC0000;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="320" y="340" width="120" height="20" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 模板6：微电网单线图

**适用场景：** 多能源接入的微电网系统。

**特点：**
- 多种能源接入
- 储能系统
- 柴发备用
- 并离网切换

```xml
<mxGraphModel>
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>

    <!-- 标题 -->
    <mxCell id="title" value="微电网单线图" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
      <mxGeometry x="200" y="20" width="400" height="30" as="geometry"/>
    </mxCell>

    <!-- 光伏系统 -->
    <mxCell id="pv" value="光伏系统&#xa;2MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="40" y="80" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 光伏逆变器 -->
    <mxCell id="pv_inv" value="逆变器&#xa;AC 2MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="160" y="80" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头 -->
    <mxCell id="arrow1" edge="1" parent="1" source="pv" target="pv_inv">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 微电网母线 -->
    <mxCell id="micro_bus" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
      <mxGeometry x="280" y="60" width="300" height="220" as="geometry"/>
    </mxCell>

    <mxCell id="micro_bus_label" value="微电网母线 400V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="290" y="65" width="120" height="20" as="geometry"/>
    </mxCell>

    <!-- 箭头：逆变器到母线 -->
    <mxCell id="arrow2" edge="1" parent="1" source="pv_inv" target="micro_bus">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 储能PCS -->
    <mxCell id="pcs" value="PCS&#xa;2MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="300" y="80" width="70" height="50" as="geometry"/>
    </mxCell>

    <!-- 电池簇 -->
    <mxCell id="battery" value="电池簇&#xa;4.3MWh" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="300" y="140" width="70" height="50" as="geometry"/>
    </mxCell>

    <!-- 柴发 -->
    <mxCell id="diesel" value="柴发&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="390" y="80" width="80" height="50" as="geometry"/>
    </mxCell>

    <!-- 负载 -->
    <mxCell id="load" value="微电网负载&#xa;峰值 1MW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="390" y="160" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- EMS -->
    <mxCell id="ems" value="EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=9" vertex="1" parent="1">
      <mxGeometry x="300" y="210" width="50" height="30" as="geometry"/>
    </mxCell>

    <!-- 箭头：PCS到母线 -->
    <mxCell id="arrow3" edge="1" parent="1" source="pcs" target="micro_bus">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- STS并离网切换 -->
    <mxCell id="sts" value="STS&#xa;并离网切换" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="340" y="300" width="100" height="50" as="geometry"/>
    </mxCell>

    <!-- 箭头：母线到STS -->
    <mxCell id="arrow4" edge="1" parent="1" source="micro_bus" target="sts">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 变压器 -->
    <mxCell id="transformer" value="变压器&#xa;1250kVA" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="500" y="290" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：STS到变压器 -->
    <mxCell id="arrow5" edge="1" parent="1" source="sts" target="transformer">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 大电网 -->
    <mxCell id="main_grid" value="大电网&#xa;15kV/20kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
      <mxGeometry x="500" y="380" width="100" height="60" as="geometry"/>
    </mxCell>

    <!-- 箭头：变压器到电网 -->
    <mxCell id="arrow6" edge="1" parent="1" source="transformer" target="main_grid">
      <mxGeometry relative="1" as="geometry"/>
    </mxCell>

    <!-- 能源标注 -->
    <mxCell id="energy_note" value="多能源协调控制&#xa;光伏+储能+柴发+电网" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontColor=#666666" vertex="1" parent="1">
      <mxGeometry x="40" y="400" width="150" height="40" as="geometry"/>
    </mxCell>

  </root>
</mxGraphModel>
```

---

## 使用说明

1. **选择模板**：根据电压等级和应用场景选择对应的模板
2. **复制XML**：将模板的完整 XML 代码复制
3. **导入draw.io**：创建新文件并导入 XML
4. **自定义修改**：
   - 修改设备容量参数
   - 调整母线和设备位置
   - 添加或删除设备
5. **导出**：支持 PNG、SVG、PDF 格式导出
