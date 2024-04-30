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

def main():
	
	canv = ROOT.TCanvas("c1","c1",800,800)
	
	#~ plotPad = TPad("plotPad","plotPad",0,0.3,1,1)
	#~ style = setTDRStyle()
	#~ gStyle.SetTitleYOffset(1.45)
	#~ gStyle.SetOptStat(0)
	#~ plotPad.UseCurrentStyle()
	#~ plotPad.Draw()	
	#~ plotPad.cd()
#~ 
	#~ resPad = TPad("resPad","resPad",0,0,1,0.3)
	#~ style = setTDRStyle()
	#~ gStyle.SetTitleYOffset(1.45)
	#~ gStyle.SetTitleXOffset(1.45)
	#~ gStyle.SetOptStat(0)
	#~ resPad.UseCurrentStyle()
	#~ resPad.Draw()	
	#~ resPad.cd()
	#~ resPad.SetGrid()
	plotPad = ROOT.TPad("plotPad","plotPad",0,0,1,1)
	#~ ratioPad = TPad("ratioPad","ratioPad",0,0.,1,0.3)
	style = setTDRStyle()
	ROOT.gStyle.SetOptStat(0)
	plotPad.UseCurrentStyle()
	#~ ratioPad.UseCurrentStyle()
	plotPad.Draw()	
	#~ ratioPad.Draw()	
	plotPad.cd()
	plotPad.cd()
	#plotPad.SetGrid()
	ROOT.gStyle.SetTitleXOffset(1.45)
	ROOT.gStyle.SetTitleYOffset(1.5)



	ids = ["softMVARun2", "softMVARun3XGBMedium"]
	idNames = {"softID": "cut-based soft ID", "softMVARun2": "Run 2 soft MVA ID", "softMVARun3": "Purdue HGB", "softMVARun3XGBMedium": "Run 3 Soft Muon ID", "softMVARun3HGBMedium": "HGB Medium"}
	idColors = {"softID": ROOT.kGray, "softMVARun2": ROOT.kBlue, "softMVARun3": ROOT.kGreen+1, "softMVARun3XGBMedium": ROOT.kRed, "softMVARun3HGBMedium": ROOT.kGreen+1}
	markers= {"softMVARun2": 20, "softMVARun3": 24, "softMVARun3XGBMedium": 22, "softMVARun3HGBMedium": 24}
	
	
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
		plotPad.DrawFrame(0,0.4,30,1.2,";probe muon p_{T} [GeV]; %s"%yLabel)


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
			histData.SetMarkerStyle(markers[id])
			histMC.SetLineColor(idColors[id]+2)
			histMC.SetMarkerColor(idColors[id]+2)
			histMC.SetLineStyle(ROOT.kDashed)
			histMC.SetMarkerStyle(markers[id]+1)

			leg.AddEntry(histData, idNames[id] + " Data", "pe")
			leg.AddEntry(histMC, idNames[id] + " MC", "pe")
			
			histData.Draw("samepe")
			histMC.Draw("samepe")

		latex = ROOT.TLatex()
		latex.SetTextFont(42)
		latex.SetTextAlign(31)
		latex.SetTextSize(0.04)
		latex.SetNDC(True)
		latexCMS = ROOT.TLatex()
		latexCMS.SetTextFont(61)
		latexCMS.SetTextSize(0.055)
		latexCMS.SetNDC(True)
		latexCMSExtra = ROOT.TLatex()
		latexCMSExtra.SetTextFont(52)
		latexCMSExtra.SetTextSize(0.03)
		latexCMSExtra.SetNDC(True) 
			
		latex.DrawLatex(0.95, 0.96, "62.4 fb^{-1} (13.6 TeV)")
		
		cmsExtra = "#splitline{Preliminary}{}"
		latexCMS.DrawLatex(0.19,0.88,"CMS")
		if "Simulation" in cmsExtra:
			yLabelPos = 0.83	
		else:
			yLabelPos = 0.83	

		latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

		

		latex.DrawLatex(0.4,0.8,absetaLabels[abseta])		
		leg.Draw()	

		plotPad.RedrawAxis()
	


		canv.Print("SoftMuonEff_abseta_%s_Run3Paper.pdf"%(abseta))
		canv.Print("SoftMuonEff_abseta_%s_Run3Paper.png"%(abseta))
			
			
	
	plotPad.cd()
	plotPad.SetLogx(0)
	plotPad.SetLogy(0)
	yMax = 1.2

	yLabel = 'Muon ID efficiency'
	plotPad.DrawFrame(-2.4,0.,2.4,1.5,";probe muon #eta; %s"%yLabel)


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
		histData.SetMarkerStyle(markers[id])
		histMC.SetLineColor(idColors[id]+2)
		histMC.SetMarkerColor(idColors[id]+2)
		histMC.SetLineStyle(ROOT.kDashed)
		histMC.SetMarkerStyle(markers[id]+1)

		leg.AddEntry(histData, idNames[id] + " Data", "pe")
		leg.AddEntry(histMC, idNames[id] + " MC", "pe")
		
		histData.Draw("samepe")
		histMC.Draw("samepe")

	latex = ROOT.TLatex()
	latex.SetTextFont(42)
	latex.SetTextAlign(31)
	latex.SetTextSize(0.04)
	latex.SetNDC(True)
	latexCMS = ROOT.TLatex()
	latexCMS.SetTextFont(61)
	latexCMS.SetTextSize(0.055)
	latexCMS.SetNDC(True)
	latexCMSExtra = ROOT.TLatex()
	latexCMSExtra.SetTextFont(52)
	latexCMSExtra.SetTextSize(0.03)
	latexCMSExtra.SetNDC(True) 
		
	latex.DrawLatex(0.95, 0.96, "62.4 fb^{-1} (13.6 TeV)")
	
	cmsExtra = "#splitline{Preliminary}{}"
	latexCMS.DrawLatex(0.19,0.88,"CMS")
	if "Simulation" in cmsExtra:
		yLabelPos = 0.83	
	else:
		yLabelPos = 0.83	

	latexCMSExtra.DrawLatex(0.19,yLabelPos,"%s"%(cmsExtra))				

	

	#latex.DrawLatex(0.4,0.8,absetaLabels[abseta])		
	leg.Draw()	

	plotPad.RedrawAxis()



	canv.Print("SoftMuonEff_Run3Paper_vsEta.pdf")
	canv.Print("SoftMuonEff_Run3Paper_vsEta.png")

	
	
main()
