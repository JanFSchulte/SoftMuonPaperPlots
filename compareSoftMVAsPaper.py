from numpy import array as ar
from setTDRStyle import setTDRStyle
import ROOT
from copy import deepcopy, copy

eras = ["2022","2022_EE","2023","2023_BPix"]
lumis = {"2022": 8.0, "2022_EE": 26.2, "2023": 17.7, "2023_BPix": 9.5}
	

def lumiWeightedAverageVsPt(id, abseta):

	
	mainPath = "plots/muon/generalTracks/JPsi/Run%s/NUM_%s_DEN_TrackerMuons/efficiency/"

	f2022 = ROOT.TFile("softMuonMVA2022New/" + mainPath%("2022",id) + "NUM_%s_DEN_TrackerMuons_abseta_%s_vs_pt.root"%(id, abseta), "OPEN")
	f2022EE = ROOT.TFile("softMuonMVA2022_EENew/" + mainPath%("2022_EE",id) + "NUM_%s_DEN_TrackerMuons_abseta_%s_vs_pt.root"%(id, abseta), "OPEN")
	f2023 = ROOT.TFile("softMuonMVA2023New/" + mainPath%("2023",id) + "NUM_%s_DEN_TrackerMuons_abseta_%s_vs_pt.root"%(id, abseta), "OPEN")
	f2023BPix = ROOT.TFile("softMuonMVA2023_BPixNew/" + mainPath%("2023_BPix",id) + "NUM_%s_DEN_TrackerMuons_abseta_%s_vs_pt.root"%(id, abseta), "OPEN")

	g2022 = f2022.Get("g_1_Simulation")
	g2022EE = f2022EE.Get("g_1_Simulation")
	g2023 = f2023.Get("g_1_Simulation")
	g2023BPix = f2023BPix.Get("g_1_Simulation")

	graph = ROOT.TGraphAsymmErrors()
	
	for i in range(0, g2022.GetN()):
		x = g2022.GetPointX(i)
		y = (g2022.GetPointY(i)*8.0 + g2022EE.GetPointY(i)*26.2 + g2023.GetPointY(i)*17.7 + g2023BPix.GetPointY(i)*9.5) / (61.4)
		exLow = g2022.GetErrorXlow(i) 
		exHigh = g2022.GetErrorXhigh(i) 
		eyLow = (g2022.GetErrorYlow(i)*8.0 + g2022EE.GetErrorYlow(i)*26.2 + g2023.GetErrorYlow(i)*17.7 + g2023BPix.GetErrorYlow(i)*9.5) / (61.4)
		eyHigh = (g2022.GetErrorYhigh(i)*8.0 + g2022EE.GetErrorYhigh(i)*26.2 + g2023.GetErrorYhigh(i)*17.7 + g2023BPix.GetErrorYhigh(i)*9.5) / (61.4)
		
		graph.SetPoint(i, x, y)
		graph.SetPointError(i, exLow, exHigh, eyLow, eyHigh)
		
	return deepcopy(graph)
	
def lumiWeightedAverageVsEta(id):

	
	mainPath = "plots/muon/generalTracks/JPsi/Run%s/NUM_%s_DEN_TrackerMuons/efficiency/"

	f2022 = ROOT.TFile("softMuonMVA2022New/" + mainPath%("2022",id) + "NUM_%s_DEN_TrackerMuons_pt2_1_vs_eta.root"%(id), "OPEN")
	f2022EE = ROOT.TFile("softMuonMVA2022_EENew/" + mainPath%("2022_EE",id) + "NUM_%s_DEN_TrackerMuons_pt2_1_vs_eta.root"%(id), "OPEN")
	f2023 = ROOT.TFile("softMuonMVA2023New/" + mainPath%("2023",id) + "NUM_%s_DEN_TrackerMuons_pt2_1_vs_eta.root"%(id), "OPEN")
	f2023BPix = ROOT.TFile("softMuonMVA2023_BPixNew/" + mainPath%("2023_BPix",id) + "NUM_%s_DEN_TrackerMuons_pt2_1_vs_eta.root"%(id), "OPEN")

	g2022 = f2022.Get("g_1_Simulation")
	g2022EE = f2022EE.Get("g_1_Simulation")
	g2023 = f2023.Get("g_1_Simulation")
	g2023BPix = f2023BPix.Get("g_1_Simulation")

	graph = ROOT.TGraphAsymmErrors()
	
	for i in range(0, g2022.GetN()):
		x = g2022.GetPointX(i)
		y = (g2022.GetPointY(i)*8.0 + g2022EE.GetPointY(i)*26.2 + g2023.GetPointY(i)*17.7 + g2023BPix.GetPointY(i)*9.5) / (61.4)
		exLow = g2022.GetErrorXlow(i) 
		exHigh = g2022.GetErrorXhigh(i) 
		eyLow = (g2022.GetErrorYlow(i)*8.0 + g2022EE.GetErrorYlow(i)*26.2 + g2023.GetErrorYlow(i)*17.7 + g2023BPix.GetErrorYlow(i)*9.5) / (61.4)
		eyHigh = (g2022.GetErrorYhigh(i)*8.0 + g2022EE.GetErrorYhigh(i)*26.2 + g2023.GetErrorYhigh(i)*17.7 + g2023BPix.GetErrorYhigh(i)*9.5) / (61.4)
		
		graph.SetPoint(i, x, y)
		graph.SetPointError(i, exLow, exHigh, eyLow, eyHigh)
		
	return deepcopy(graph)


def ratio(data, mc):


	graph = ROOT.TGraphAsymmErrors()
	
	for i in range(0, data.GetN()):
		x = data.GetPointX(i)
		y = data.GetPointY(i)/mc.GetPointY(i)
		exLow = data.GetErrorXlow(i) 
		exHigh = data.GetErrorXhigh(i) 
		eyLow = (data.GetErrorYlow(i)**2 + mc.GetErrorYlow(i)**2)**0.5
		eyHigh =  (data.GetErrorYhigh(i)**2 + mc.GetErrorYhigh(i)**2)**0.5
		
		graph.SetPoint(i, x, y)
		graph.SetPointError(i, exLow, exHigh, eyLow, eyHigh)
		
	return deepcopy(graph)

def main():
	
	canv = ROOT.TCanvas("c1","c1",800,800)
	
	plotPad = ROOT.TPad("plotPad","plotPad",0,0.3,1,1)
	ratioPad = ROOT.TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	ROOT.gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	ratioPad.Draw()	
	plotPad.cd()
	plotPad.cd()

	ROOT.gStyle.SetTitleXOffset(1.45)
	ROOT.gStyle.SetTitleYOffset(1.5)



	ids = ["softMVARun2", "softMVARun3XGBMedium"]
	idNames = {"softID": "cut-based soft ID", "softMVARun2": "Run 2 soft MVA ID", "softMVARun3": "Purdue HGB", "softMVARun3XGBMedium": "Run 3 Soft Muon ID", "softMVARun3HGBMedium": "HGB Medium"}
	idColors = {"softID": ROOT.kGray, "softMVARun2": ROOT.TColor.GetColor("#5790fc"), "softMVARun3": ROOT.kGreen+1, "softMVARun3XGBMedium": ROOT.TColor.GetColor("#e42536"), "softMVARun3HGBMedium": ROOT.TColor.GetColor("#e42536")}
	idMarkers = {"softMVARun2": 20, "softMVARun3": 24, "softMVARun3XGBMedium": 22, "softMVARun3HGBMedium": 24}
	idMarkersMC = {"softMVARun2": 24, "softMVARun3": 24, "softMVARun3XGBMedium": 26, "softMVARun3HGBMedium": 24}
	
	
	absetabins = ["1","2","3"]
	absetaLabels = {
		"1":"0 < |#eta| < 0.9",
		"2":"0.9 < |#eta| < 1.2",
		"3":"1.2 < |#eta| < 2.4",
	}
	

	resultPath = "softMuonMVARun3New/"
	mainPath = "plots/muon/generalTracks/JPsi/Run3/NUM_%s_DEN_TrackerMuons/efficiency/"

	
	for abseta in absetabins:

		plotPad.cd()
		plotPad.SetLogx(0)
		plotPad.SetLogy(0)
		yMax = 1.2

		yLabel = 'Muon ID efficiency'
		frame = plotPad.DrawFrame(2,0.3,10,1.2,";probe muon p_{T} [GeV]; %s"%yLabel)
		frame.GetYaxis().SetTitleFont(42)
		frame.GetYaxis().SetTitleSize(0.05)
		frame.GetYaxis().SetTitleOffset(1.35)
		frame.GetYaxis().SetLabelFont(42)
		frame.GetYaxis().SetLabelSize(0.06)
		frame.GetXaxis().SetTitleSize(0.0)
		frame.GetXaxis().SetLabelSize(0.0)

		leg = ROOT.TLegend(0.42, 0.72, 0.89, 0.92,"","brNDC")
		leg.SetFillColor(10)
		leg.SetFillStyle(0)
		leg.SetLineColor(10)
		leg.SetShadowColor(0)
	
		histsData = []
		histsMC = []
		for id in ids:
			
			f = ROOT.TFile(resultPath + mainPath%(id) + "NUM_%s_DEN_TrackerMuons_abseta_%s_vs_pt.root"%(id, abseta), "OPEN")
			histsData.append(deepcopy(f.Get("g_0_Data").Clone(id)))
			histsMC.append(deepcopy(lumiWeightedAverageVsPt(id,abseta)))
	
		for i in range(0,len(ids)):
			id = ids[i]
			histData = histsData[i]
			histMC = histsMC[i]
			histData.SetLineColor(idColors[id])
			histData.SetMarkerColor(idColors[id])
			histData.SetMarkerStyle(idMarkers[id])
			histMC.SetLineColor(idColors[id])
			histMC.SetMarkerColor(idColors[id])
			histMC.SetLineStyle(ROOT.kDashed)
			histMC.SetMarkerStyle(idMarkersMC[id])

			leg.AddEntry(histData, idNames[id] + " Data", "pe")
			leg.AddEntry(histMC, idNames[id] + " MC", "pe")
			
			histData.Draw("samepe")
			histMC.Draw("samepe")

		latex = ROOT.TLatex()
		latex.SetTextFont(42)
		latex.SetTextAlign(31)
		latex.SetTextSize(0.05)
		latex.SetNDC(True)
		latexCMS = ROOT.TLatex()
		latexCMS.SetTextFont(61)
		latexCMS.SetTextSize(0.08)
		latexCMS.SetNDC(True)
		latexCMSExtra = ROOT.TLatex()
		latexCMSExtra.SetTextFont(52)
		latexCMSExtra.SetTextSize(0.05)
		latexCMSExtra.SetNDC(True) 
			
		latex.DrawLatex(0.95, 0.95, "62.5 fb^{-1} (13.6 TeV)")
		
		cmsExtra = "#splitline{Preliminary}{}"
		latexCMS.DrawLatex(0.19,0.85,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.77	
		else:
			yLabelPos = 0.77	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		
		latexEta = ROOT.TLatex()
		latexEta.SetTextFont(42)
		latexEta.SetTextAlign(31)
		latexEta.SetTextSize(0.06)
		latexEta.SetNDC(True)		
		if abseta == "1":
			latexEta.DrawLatex(0.39,0.7,absetaLabels[abseta])		
		else:
			latexEta.DrawLatex(0.42,0.7,absetaLabels[abseta])		
		leg.Draw()	

		plotPad.RedrawAxis()
	
		plotPad.SetBottomMargin(0.03)
		plotPad.SetTopMargin(0.06)
		plotPad.RedrawAxis()
	
		ratioPad.cd()
		ratioPad.SetTopMargin(0.03)
		ratioPad.SetBottomMargin(0.4)
		frame = ratioPad.DrawFrame(2,0.75,10,1.25,";probe muon p_{T} [GeV]; Data / MC")
		
		frame.GetYaxis().SetTitle("Data/MC")
		frame.GetXaxis().SetNoExponent(0)
		frame.GetXaxis().SetTitleFont(42)
		frame.GetXaxis().SetTitleOffset(0.925)
		frame.GetXaxis().SetTitleSize(0.18)
		frame.GetXaxis().SetLabelColor(1)
		frame.GetXaxis().SetLabelOffset(0.01)
		frame.GetXaxis().SetLabelFont(42)
		frame.GetXaxis().SetLabelSize(0.17)				
		frame.GetYaxis().SetTitleOffset(0.55)
		frame.GetYaxis().SetTitleSize(0.12)
		frame.GetYaxis().SetTitleFont(42)
		frame.GetYaxis().SetLabelSize(0.14)    
		frame.GetYaxis().SetLabelOffset(0.007)    
		frame.GetYaxis().SetLabelFont(42)    
		frame.GetYaxis().SetNdivisions(505)  
		
		
		l = ROOT.TLine(2,1,10,1)
		l.SetLineStyle(ROOT.kDashed)
		l.Draw("same")


		ratios = []
		for i in range(0,len(ids)):
			id = ids[i]
			histData = histsData[i]
			histMC = histsMC[i]
			r = ratio(histData,histMC)
			r.SetLineColor(idColors[id])
			r.SetMarkerColor(idColors[id])
			r.SetMarkerStyle(idMarkers[id])
			ratios.append(r)
			
		for i in range(0,len(ids)):
			ratios[i].Draw("samepe")

		canv.Print("SoftMuonEff_abseta_%s_Run3Paper.pdf"%(abseta))
		canv.Print("SoftMuonEff_abseta_%s_Run3Paper.png"%(abseta))
			
			
	
	plotPad.cd()
	plotPad.SetLogx(0)
	plotPad.SetLogy(0)
	yMax = 1.2

	yLabel = 'Muon ID efficiency'
	frame = plotPad.DrawFrame(-2.4,0.3,2.4,1.5,";probe muon #eta; %s"%yLabel)
	frame.GetYaxis().SetTitleFont(42)
	frame.GetYaxis().SetTitleSize(0.05)
	frame.GetYaxis().SetTitleOffset(1.35)
	frame.GetYaxis().SetLabelFont(42)
	frame.GetYaxis().SetLabelSize(0.06)
	frame.GetXaxis().SetTitleSize(0.0)
	frame.GetXaxis().SetLabelSize(0.0)

	leg = ROOT.TLegend(0.42, 0.72, 0.89, 0.92,"","brNDC")
	leg.SetFillColor(10)
	leg.SetFillStyle(0)
	leg.SetLineColor(10)
	leg.SetShadowColor(0)

	histsData = []
	histsMC = []
	for id in ids:
		
		f = ROOT.TFile(resultPath + mainPath%(id) + "NUM_%s_DEN_TrackerMuons_pt2_1_vs_eta.root"%(id), "OPEN")
		histsData.append(deepcopy(f.Get("g_0_Data").Clone(id)))
		histsMC.append(deepcopy(lumiWeightedAverageVsEta(id)))

	for i in range(0,len(ids)):
		id = ids[i]
		histData = histsData[i]
		histMC = histsMC[i]
		histData.SetLineColor(idColors[id])
		histData.SetMarkerColor(idColors[id])
		histData.SetMarkerStyle(idMarkers[id])
		histMC.SetLineColor(idColors[id])
		histMC.SetMarkerColor(idColors[id])
		histMC.SetLineStyle(ROOT.kDashed)
		histMC.SetMarkerStyle(idMarkersMC[id])

		leg.AddEntry(histData, idNames[id] + " Data", "pe")
		leg.AddEntry(histMC, idNames[id] + " MC", "pe")
		
		histData.Draw("samepe")
		histMC.Draw("samepe")

	latex = ROOT.TLatex()
	latex.SetTextFont(42)
	latex.SetTextAlign(31)
	latex.SetTextSize(0.05)
	latex.SetNDC(True)
	latexCMS = ROOT.TLatex()
	latexCMS.SetTextFont(61)
	latexCMS.SetTextSize(0.08)
	latexCMS.SetNDC(True)
	latexCMSExtra = ROOT.TLatex()
	latexCMSExtra.SetTextFont(52)
	latexCMSExtra.SetTextSize(0.05)
	latexCMSExtra.SetNDC(True) 
		
	latex.DrawLatex(0.95, 0.95, "62.5 fb^{-1} (13.6 TeV)")
	
	cmsExtra = "#splitline{Preliminary}{}"
	latexCMS.DrawLatex(0.19,0.85,"CMS")
	if "Simulation" in cmsExtra:
		yLabelPos = 0.77	
	else:
		yLabelPos = 0.77	

	latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

	

	#latex.DrawLatex(0.4,0.8,absetaLabels[abseta])		
	leg.Draw()	


	plotPad.SetBottomMargin(0.03)
	plotPad.SetTopMargin(0.06)
	plotPad.RedrawAxis()

	ratioPad.cd()
	ratioPad.SetTopMargin(0.03)
	ratioPad.SetBottomMargin(0.4)
	frame = ratioPad.DrawFrame(-2.4,0.5,2.4,1.5,";probe muon #eta; Data / MC")
	
	frame.GetYaxis().SetTitle("Data/MC")
	frame.GetXaxis().SetNoExponent(0)
	frame.GetXaxis().SetTitleFont(42)
	frame.GetXaxis().SetTitleOffset(0.925)
	frame.GetXaxis().SetTitleSize(0.18)
	frame.GetXaxis().SetLabelColor(1)
	frame.GetXaxis().SetLabelOffset(0.01)
	frame.GetXaxis().SetLabelFont(42)
	frame.GetXaxis().SetLabelSize(0.17)				
	frame.GetYaxis().SetTitleOffset(0.55)
	frame.GetYaxis().SetTitleSize(0.12)
	frame.GetYaxis().SetTitleFont(42)
	frame.GetYaxis().SetLabelSize(0.14)    
	frame.GetYaxis().SetLabelOffset(0.007)    
	frame.GetYaxis().SetLabelFont(42)    
	frame.GetYaxis().SetNdivisions(505)  
	
	
	l = ROOT.TLine(-2.4,1,2.4,1)
	l.SetLineStyle(ROOT.kDashed)
	l.Draw("same")


	ratios = []
	for i in range(0,len(ids)):
		id = ids[i]
		histData = histsData[i]
		histMC = histsMC[i]
		r = ratio(histData,histMC)
		r.SetLineColor(idColors[id])
		r.SetMarkerColor(idColors[id])
		r.SetMarkerStyle(idMarkers[id])
		ratios.append(r)
		
	for i in range(0,len(ids)):
		ratios[i].Draw("samepe")

	canv.Print("SoftMuonEff_Run3Paper_vsEta.pdf")
	canv.Print("SoftMuonEff_Run3Paper_vsEta.png")

	
	
main()
